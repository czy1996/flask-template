from . import BaseDocument, db


class Todo(BaseDocument):
    counter = db.SequenceField()
    title = db.StringField()
    is_deleted = db.BooleanField(default=False, required=True)
