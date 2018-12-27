from flask import Blueprint, current_app, jsonify, request

# 这么写是相对导入，虽然可以，但是感觉有毒
# 等价于 from app.models
from ..models.Todo import Todo, TodoSchema

from .utils import validate_post

main = Blueprint('todo', __name__)


@main.route('/', methods=['GET'], strict_slashes=False)
def get_collection():
    result = {
        'status_code': 0,
    }

    # 我觉得这种程度的封装就已经够了
    # 但可否进一步封装成 .jsonify(todos, many=True), 自动附上 status_code
    # 对于需要 filter 的 api，后续可能还要加一层装饰器校验/清洗，使这里的 args 能够直接用
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    result['data'] = Todo.objects.to_collection_dict(page, per_page, '.get_collection')

    return jsonify(result)


@main.route('/', methods=['POST'], strict_slashes=False)
@validate_post
def add_one():
    result = {
        'status_code': 0,
    }  # 什么时候把这段也抽象出去
    todo = Todo.new(request.json)
    result['data'] = todo.to_dict()
    return jsonify(result)


@main.route('/<int:todo_id>', methods=['GET'])
def get_one(todo_id):
    response = {
        'status_code': 0,
    }

    todo = Todo.first(counter=todo_id)

    if not todo:
        response['status_code'] = 1
        return jsonify(response)  # 这段怎么抽出去？

    response['data'] = todo.to_dict()

    return jsonify(response)


@main.route('/<int:todo_id>', methods=['POST'])
@validate_post
def update_one(todo_id):
    response = {
        'status_code': 0,
    }

    # 待重构
    todo = Todo.first(counter=todo_id)
    todo.update(**request.json)
    response['data'] = todo.to_dict()
    return jsonify(response)


@main.route('/<int:todo_id>', methods=['DELETE'])
def delete_one(todo_id):
    response = {
        'status_code': 0,
    }

    # 待重构
    todo = Todo.first(counter=todo_id)
    todo.delete()
    return jsonify(response)
