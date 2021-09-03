from flask import Blueprint

api = Blueprint('user', __name__, url_prefix='/user')  # 创建一个蓝图


@api.route('')
def index():
    return 'here is user v1.'


@api.route('/hello', methods=['GET', 'POST'])  # 多种请求类型
def hello():
    return 'hello user v1.'
