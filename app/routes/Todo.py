from flask import Blueprint, current_app, jsonify

from models import Todo

main = Blueprint('todo', __name__)


@main.route('/all')
def add():
    result = {
        'status_code': 0,
    }
    todos = Todo.objects
    result['data'] = [todo.to_dict() for todo in todos]
    return jsonify(result)
