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
