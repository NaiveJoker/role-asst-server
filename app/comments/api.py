from flask import jsonify, request
from app.comments.model import Comments
from app.common import Common


def init_api(app):
    @app.route('/comments', methods=['GET'])
    def getComments():
        comments = Comments.getAll(Comments)
        output = []
        for comment in comments:
            output.append(Comments.output(Comments, comment))
        return jsonify(Common.trueReturn(Common, output))

    @app.route('/comments', methods=['POST'])
    def addComments():
        username = request.form.get('username')
        content = request.form.get('comments')
        if username is None:
            return jsonify(Common.falseReturn(Common, None, '尚未登录，无法评论'))
        elif content == "":
            # 评论不能为空
            return jsonify(Common.falseReturn(Common, None, '内容为空，评论失败'))
        else:
            comment = Comments(username=username, content=content)
            result = Comments.add(Comments, comment)
            return getComments()
