from flask import Blueprint

api = Blueprint('admin', __name__, url_prefix='/admin')  # 创建一个蓝图


@api.route('')
def index():
    return 'here is admin v1.'


@api.route('/hello', methods=['POST'])
def hello():
    return 'hello admin v1.'
