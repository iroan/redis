# 业务过程
# 1. 输入用户名,密码
# 2. 密码加密
# 3. 判断Redis中是否记录了用户名,如果有则成功
# 4. 如果Redis中没有用户名,则到MySQL中查阅
# 5. 从MySQL中查阅成功后,讲用户名记录到Redis中

from redisHelper import RedisHelper
import hashlib


class SimulateSignin():
    def __init__(self):
        self.name = input('请输入登录名:')
        pwd = input('请输入登录密码:')

        sha1 = hashlib.sha1()
        sha1.update(pwd.encode())
        self.pwd = sha1.hexdigest()

        print('name = %s,password = %s',self.name,self.pwd)

    def runRedis(self):
        try:
            r = RedisHelper()
            if r.get('uname') == self.name:
                print('登录成功')
            else:
                print('Redis数据库中没有找到数据,前往MySQL中查找')
                self.runMysql()
        except Exception as e:
            print(e.args)

    def runMysql(self):
        from msqlHelper import MysqlHelper
        m = MysqlHelper('root', 'iroanMYS47')
        res = m.fetchone('select password from user where name = %s;', [self.name])
        print('password in mysql = %s',res)
        if res[0] == self.pwd:
            print('登录成功')

if __name__ == '__main__':
    s = SimulateSignin()
    s.runRedis()