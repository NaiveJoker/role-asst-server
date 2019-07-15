# MySQL用户相关内容
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost:3306'
DB_DB = 'role_asst'

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
UPLOAD_FOLDER = "upload"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + \
    ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
