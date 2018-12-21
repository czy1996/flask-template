from flask_mongoengine import MongoEngine

db = MongoEngine()


class Todo(db.Document):
    title = db.StringField()
