from . import BaseDocument, db, BaseSchema, ma


class TodoSchema(BaseSchema):
    title = ma.String(required=True)


_schema = TodoSchema()


class Todo(BaseDocument):
    _schema = _schema
    counter = db.SequenceField()
    title = db.StringField()
    is_deleted = db.BooleanField(default=False, required=True)
