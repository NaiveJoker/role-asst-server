import base64
import hashlib
import random
import string


class UserService():
    # 利用hashlib对输入的密码进行加密
    @staticmethod
    def password(pwd, salt):
        m = hashlib.md5()
        str = "{}-{}".format(base64.encodebytes(pwd.encode('utf-8')), salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def authcode(staff):
        m = hashlib.md5()
        str = "{}-{}-{}-{}".format(staff.s_id,
                                   staff.s_name, staff.passwd, staff.level)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def salt(length=16):
        str = string.ascii_letters+string.digits
        return ''.join([random.choice(str) for i in range(length)])
