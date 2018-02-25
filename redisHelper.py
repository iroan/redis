import redis

class RedisHelper():
    def __init__(self,host='localhost',port=6379):
        self._redis = redis.StrictRedis(host,port)
    def get(self,key):
        if self._redis.exists(key):
            return self._redis.get(key)
        else:
            return ''
    def set(self,key,value):
        self._redis.set(key,value)

if __name__ == '__main__':
    r = RedisHelper()
    r.set('name3','wkx')
    print(r.get('name3'))