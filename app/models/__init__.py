import json

from flask_mongoengine import MongoEngine

db = MongoEngine()


class BaseDocument(db.Document):
    meta = {
        'abstract': True,
    }

    def to_dict(self):
        # use_db_fields 意义不明
        d = json.loads(self.to_json())
        id_ = d.pop('_id')['$oid']
        d['oid'] = id_

        id_ = d.pop('counter')
        d['id'] = id_
        return d


class Todo(BaseDocument):
    counter = db.SequenceField()
    title = db.StringField()
    is_deleted = db.BooleanField(default=False, required=True)
