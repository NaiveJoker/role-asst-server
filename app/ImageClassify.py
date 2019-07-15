from werkzeug.utils import secure_filename
import base64
import time
from app.strUtil import Pic_str
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
from flask import jsonify, request
from aip import AipImageClassify
import os

# 调用百度AI的人工智能识别模块,具体查看相关
# 使用前文件需更名为AipImageClassify.py，或在__init__.py中文件名称
APP_ID =
API_KEY =
SECRET_KEY =

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])


def init_api(app):
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 上传文件
    @app.route('/upload', methods=['POST'], strict_slashes=False)
    def api_upload():
        file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        img = request.files['image']
        if img and allowed_file(img.filename):
            fname = img.filename
            ext = fname.rsplit('.', 1)[1]
            new_filename = Pic_str().create_uuid() + '.' + ext
            img.save(os.path.join(file_dir, new_filename))
            image = get_file_content('app/upload/'+new_filename)
            return client.advancedGeneral(image)
        else:
            return jsonify({"error": 1001, "msg": "上传失败"})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)
