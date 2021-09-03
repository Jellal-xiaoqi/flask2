from flask import Flask
from app import v1, v2

app = Flask(__name__)  # 创建Flask的主app
app.register_blueprint(v1.bp)  # 注册蓝图
app.register_blueprint(v2.bp)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
