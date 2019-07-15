from flask import jsonify, request, Response, make_response
from app.users.model import Users
from app.common import Common
from .. import userAuth


def init_api(app):
    # 注册路由，根据确定是否注册
    @app.route('/signup', methods=['POST'])
    def signup():
        email = request.form.get('email')
        username = request.form.get('username')
        passwd = request.form.get('password')
        name_exist = Users.get_byname(Users, username)
        email_exist = Users.get_byemail(Users, email)
        if name_exist or email_exist:
            return jsonify(Common.falseReturn(Common, None, '邮箱或用户名已存在！'))
        else:
            spasswd = userAuth.UserService.password(passwd, email)
            user = Users(email=email, username=username, passwd=spasswd)
            result = Users.add(Users, user)
            return jsonify(Common.trueReturn(Common, result, '注册成功'))

    # 登录相关，返回登录用户名和成功信息
    @app.route('/login', methods=['POST'])
    def login():
        email = request.form.get('email')
        passwd = request.form.get('password')
        user = Users.get_byemail(Users, email)
        if user is None:
            return jsonify(Common.falseReturn(Common, None, '账号或密码不正确'))
        else:
            spasswd = userAuth.UserService.password(passwd, email)
            if user.passwd == spasswd:
                return jsonify(Common.trueReturn(Common, user.username, '登录成功'))
            else:
                return jsonify(Common.falseReturn(Common, None, '账号或密码不正确'))

    # 获取已注册的所有用户信息（用于测试
    @app.route('/users', methods=['GET'])
    def getUsers():
        users = Users.getAll(Users)
        output = []
        for user in users:
            output.append(Users.output(Users, user))
        return jsonify(Common.trueReturn(Common, output))
