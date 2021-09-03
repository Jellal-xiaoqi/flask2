from flask import Blueprint
from app.v2 import admin, user

bp = Blueprint('v2', __name__, url_prefix='/v2')  # 创建父蓝图v2

bp.register_blueprint(admin.api)  # 注册子蓝图admin
bp.register_blueprint(user.api)  # 注册子蓝图user


@bp.route('')
def index():
    """父蓝图视图函数"""
    return 'here is v2.'
