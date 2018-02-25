# 业务过程
# 1. 输入用户名,密码
# 2. 密码加密
# 3. 判断Redis中是否记录了用户名,如果有则成功
# 4. 如果Redis中没有用户名,则到MySQL中查阅
# 5. 从MySQL中查阅成功后,讲用户名记录到Redis中

from redisHelper import RedisHelper
import hashlib

name = input('请输入登录名:')
pwd = input('请输入登录密码:')

sha1 = hashlib.sha1()
sha1.update(pwd)
pwd1 = sha1.hexdigest()

try:
    r = RedisHelper()
    if r.get('uname') == name:
        print('ok')
    else:
        pass
except Exception as e:
    print(e.args)

