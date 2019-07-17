from werkzeug.utils import secure_filename
import base64
import time
from app.strUtil import Pic_str
from app.common import Common
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
from flask import jsonify, request
from aip import AipFace
import os
import base64
import urllib
import re

# 调用百度AI的人脸搜索模块
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipFace(APP_ID, API_KEY, SECRET_KEY)


app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])


def init_api(app):
    def get_file_content(filePath):
        with open(filePath, 'rb') as image_file:
            # 图片需进行base64编码
            return base64.b64encode(image_file.read())

    # 上传文件
    @app.route('/upload', methods=['POST'], strict_slashes=False)
    def api_upload():
        # 获取存储路径
        file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # 获取图片和图片名称
        img = request.files['screenshot']
        filename = request.form.get("filename")
        print(img)
        if img:
            if img and allowed_file(filename):
                fname = filename
                ext = fname.rsplit('.', 1)[1]
                new_filename = Pic_str().create_uuid() + '.' + ext
                img.save(os.path.join(file_dir, new_filename))
                # 图片需要转成BASE64
                image = get_file_content('app/upload/'+new_filename)
            # BASE64转字符串
            image64 = str(image, 'utf-8')
            imageType = "BASE64"
            groupIdList = "GamesOfThrone"
            # 设置人脸识别参数
            options = {}
            options["max_face_num"] = 5
            options["match_threshold"] = 70
            options["max_user_num"] = 5
            # 图像识别返回内容
            return client.multiSearch(image64, imageType, groupIdList, options)
        else:
            return jsonify(Common.falseReturn(Common, None, "图片上传失败"))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)
