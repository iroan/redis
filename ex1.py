import redis

try:
    r = redis.StrictRedis(host='localhost',port=6379)
except Exception as e:
    print(e.args)

def ex_string():
    # 练习string
    r.set('name', 'wangkaixuan')
    print(r.get('name').decode())

    r.set('height', 175)
    r.incr('height')
    r.incr('height')
    r.incr('height')
    print(r.get('height').decode())

    r.set('inputing', 'input...', ex=2)
    print(r.get('inputing').decode())
    print(r.ttl('inputing'))
    import time
    time.sleep(2)
    print(r.get('inputing').decode())


def ex_list():
    r.lpush('name1', 'wangkaixuan')
    r.lpush('name1', 'wangkaijun')
    r.lpush('name1', 'chengangrong')
    r.rpush('name1', 'longhao')
    print(r.lrange('name1', 0, -1))
    # r.lpop(name='name1')
    # r.lpop(name='name1')
    # r.rpop(name='name1')
    # r.rpop(name='name1')

    print(r.llen('name1'))



