from flask import Blueprint, current_app, jsonify, request

# 这么写是相对导入，虽然可以，但是感觉有毒
# 等价于 from app.models
from ..models import Todo

main = Blueprint('todo', __name__)


@main.route('/')
def add():
    result = {
        'status_code': 0,
    }
    todos = Todo.objects
    result['data'] = [todo.to_dict() for todo in todos]
    return jsonify(result)


@main.route('/<int:todo_id>', methods=['GET', 'POST'])
def todo(todo_id):
    response = {
        'status_code': 0,
    }

    todo = Todo.objects(counter=todo_id).first()

    if not todo:
        response['status_code'] = 1
        return jsonify(response)

    if request.method == 'GET':
        response['data'] = todo.to_dict()
        return jsonify(response)
    else:
        todo.title = request.json['title']
        todo.save()
        return jsonify(response)
