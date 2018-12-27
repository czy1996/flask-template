import datetime

from . import BaseDocument, db, BaseSchema, ma


class TodoSchema(BaseSchema):
    # 增必须要有点字段
    title = ma.String(required=True)


_schema = TodoSchema


class Todo(BaseDocument):
    schema = _schema

    # counter 模拟了一个自增式的数字 id，用它来作为 api 的 id
    # 这显然是一个公共字段，但是由于 mongoengine 实现的原因，不能把它放入 BaseDocument
    counter = db.SequenceField()
    title = db.StringField()
