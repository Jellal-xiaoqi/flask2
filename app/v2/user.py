import asyncio

from flask import Blueprint

api = Blueprint('user', __name__, url_prefix='/user')  # 创建一个蓝图


@api.get('')
def index():
    return 'here is user v2.'


@api.post('/hello')
async def hello():
    await asyncio.sleep(1)
    return 'hello user v2.'
