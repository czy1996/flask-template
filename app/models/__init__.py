import json

from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

db = MongoEngine()
ma = Marshmallow()


class BaseDocument(db.Document):
    meta = {
        'abstract': True,
    }

    def to_dict(self):
        # use_db_fields 意义不明
        d = self._schema.dump(self)
        return d

    @classmethod
    def all(cls, **kwargs):
        return cls.objects(is_deleted=False, **kwargs)

    @classmethod
    def first(cls, **kwargs):
        return cls.all(**kwargs).first()

    def delete(self, hard_delete=False, **kwargs):
        if hard_delete:
            super().delete(**kwargs)
        else:
            self.is_deleted = True
            self.save()


class BaseSchema(ma.Schema):
    # counter 维护了自增的整数 id
    # 希望 dump 出的 json ，id 其实是 counter 值
    # load 是什么行为？
    id = ma.Integer(attribute='counter', dump_only=True)
