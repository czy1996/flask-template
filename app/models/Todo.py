import datetime

from . import BaseDocument, db, BaseSchema, ma


class TodoSchema(BaseSchema):
    # 增必须要有点字段
    title = ma.String(required=True)

    # 只导出不修改
    created_at = ma.DateTime(dump_only=True)


_schema = TodoSchema()


class Todo(BaseDocument):
    _schema = _schema
    counter = db.SequenceField()
    title = db.StringField()
    is_deleted = db.BooleanField(default=False, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
