class Common:
    #请求成功返回信息
    def trueReturn(self, data, msg="请求成功"):
        return {
            "status": 1,
            "data": data,
            "msg": msg
        }
    #请求失败返回信息
    def falseReturn(self, data, msg="请求失败"):
        return {
            "status": 0,
            "data": data,
            "msg": msg
        }
