from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import path as op
db = SQLAlchemy()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # 解决跨域问题
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    db.init_app(app)
    # 生成应用
    from app.comments.api import init_api
    init_api(app)
    from app.users.api import init_api
    init_api(app)
    from app.AipImageClassify import init_api
    init_api(app)
    return app
