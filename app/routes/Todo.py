from flask import Blueprint, current_app, jsonify

# 这么写是相对导入，虽然可以，但是感觉有毒
# 等价于 from app.models
from ..models import Todo

main = Blueprint('todo', __name__)


@main.route('/all')
def add():
    result = {
        'status_code': 0,
    }
    todos = Todo.objects
    result['data'] = [todo.to_dict() for todo in todos]
    return jsonify(result)
