import datetime

from flask import current_app as app
from flask import url_for
from mongoengine import Q

from flask_mongoengine import MongoEngine, BaseQuerySet
from flask_marshmallow import Marshmallow

db = MongoEngine()
ma = Marshmallow()


class _QuerySet(BaseQuerySet):
    """
    卧槽这个 _ 实在是太 2b 了，但是 Base 已经被占用了容易引起误会
    这个类的作用：
    - 默认检索 is_delete=False
    - 一律将 id 转换成 counter 进行查询(会不会影响效率?)
    - 实现 to_collection_dict, 调用方式 类似于 User.objects(created_at__lt=asdkfasd).to_collection_dict()
    """

    def __init__(self, document, collection):
        super().__init__(document, collection)
        # 默认查询未删除
        # self._query_obj = Q(is_deleted=False)
        # 会导致 bug，暂缓实现
        pass

    def __call__(self, *args, include_deleted=False, **kwargs):
        # 默认检索 is_delete=False
        # 但是这样做, 除了代码看上稍微干净一点，有别的好处吗？
        # 三种情况，只返回未删除 objects()
        # 只返回已删除 objects(is_deleted=True)
        # 返回所有 objects(include_deleted=True)
        if kwargs.get('is_deleted', False):
            # 只返回删除的
            return super().__call__(*args, **kwargs)
        if include_deleted:
            # 返回所有的
            kwargs.pop('is_deleted')
        else:
            # 不返回删除的
            kwargs['is_deleted'] = False

        return super().__call__(*args, **kwargs)

    def to_collection_dict(self, page=1, per_page=10, endpoint=None):
        pagination = self.paginate(page, per_page)
        data = {
            'items': [item.to_dict() for item in pagination.items],  # 想交给 schmea(many=True) 生成，但目前没有很好的办法
            '_meta': {
                'current_page': pagination.page,
                'next_page': pagination.next_num,
                'prev_page': pagination.prev_num,
                'per_page': pagination.per_page,
                'total_pages': pagination.pages,
                'total_items': pagination.total,
            },
            '_link': {
                'self': url_for(endpoint, page=page, per_page=per_page),
                'next': url_for(endpoint, page=pagination.next_num, per_page=per_page) if pagination.has_next else None,
                'prev': url_for(endpoint, page=pagination.prev_num, per_page=per_page) if pagination.has_prev else None
            } if endpoint else None
        }
        return data


class BaseDocument(db.Document):
    """
    目前的实现方法是，Document 进行各项操作之前，使用 schema 校验数据
    导出数据也使用 schema 实现
    """
    meta = {
        'abstract': True,
        'queryset_class': _QuerySet
    }

    # 公共字段
    is_deleted = db.BooleanField(default=False, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        # use_db_fields 意义不明
        d = self.schema().dump(self)
        return d

    def to_collection_dict(self, collection):
        # 卵子用都没有
        d = self.schema(many=True).dump(collection)
        return d

    @classmethod
    def all(cls, **kwargs):
        return cls.objects(**kwargs)

    @classmethod
    def first(cls, **kwargs):
        return cls.all(**kwargs).first()

    def delete(self, hard_delete=False, **kwargs):
        if hard_delete:
            super().delete(**kwargs)
        else:
            self.is_deleted = True
            self.save()

    def update(self, **kwargs):
        app.logger.debug('update called')
        valid = self.schema().load(kwargs, partial=True)  # 啥也不改，这种行为是允许的，但是遇到没见过的依然会报错
        # 自动更新修改时间
        valid['updated_at'] = datetime.datetime.now()
        return super().update(**valid)

    def clean(self):
        # 自动写入更新时间
        self.updated_at = datetime.datetime.now()

    @classmethod
    def new(cls, data):
        valid = cls.schema().load(data)
        return cls(**valid).save()


class BaseSchema(ma.Schema):
    # counter 维护了自增的整数 id
    # 希望 dump 出的 json ，id 其实是 counter 值
    # load 是什么行为？
    id = ma.Integer(attribute='counter', dump_only=True)
    # 只导出不修改
    created_at = ma.DateTime(dump_only=True)
    updated_at = ma.DateTime(dump_only=True)
