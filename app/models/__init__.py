import json

from flask_mongoengine import MongoEngine

db = MongoEngine()


class BaseDocument(db.Document):
    meta = {
        'abstract': True,
    }

    def to_dict(self):
        print(self.__dict__)
        d = json.loads(self.to_json())
        id_ = d.pop('_id')['$oid']
        d['id'] = id_
        return d


class Todo(BaseDocument):
    title = db.StringField()
