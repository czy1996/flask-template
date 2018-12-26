from flask import jsonify
from functools import wraps
from marshmallow import ValidationError


def error_response(http_code, custom_error='', status_code=1):
    payload = {
        'status_code': status_code,
        'error': custom_error,
    }
    response = jsonify(payload)
    response.status_code = http_code
    return response


def validate_post(f):
    """
    如果请求处理过程中，发生 ma 的校验错误，直接返回错误信息
    :param f:
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            ret_val = f(*args, **kwargs)
        except ValidationError as e:
            return error_response(400, e.messages, 1)
        return ret_val

    return wrapper
