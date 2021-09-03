import asyncio

from flask import Blueprint

api = Blueprint('admin', __name__, url_prefix='/admin')  # 创建一个蓝图


@api.get('')  # 快捷路由装饰器
def index():
    return 'here is admin v2.'


@api.post('/hello')
async def hello():
    """异步视图"""
    await asyncio.sleep(1)
    return 'hello admin v2.'
