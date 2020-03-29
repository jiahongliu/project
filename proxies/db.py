'''
代理存储模块
'''

import redis
from random import choice

MAX_SCORE=100.0
MIN_SCORE=0.0
INITIAL_SCORE=10.0
REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_PASSWORD=123456
REDIS_KEY='proxies'


# class PoolEmptyError(object):
#     print()

#存储代理----------存储模块
class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    #定义一个添加数据的方法
    def add(self,proxy,score=INITIAL_SCORE):
        #如果数据库中没有则添加数据
        if not self.db.zscore(REDIS_KEY,proxy):
            mapping={proxy:score}
            return self.db.zadd(REDIS_KEY,mapping)

    #定义一个方法随机获得代理
    def random(self):
        #result取最高分数代理
        result=self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        #最高分数存在,随机选择其中一个返回
        if len(result):
            return choice(result)
        else:
            #result按照分数排名取代理
            result=self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            #数据库空抛出异常
            else:
                return '代理为空'

    #定义一个方法代理值减1  低于0删除
    def decrease(self,proxy):
        score=self.db.zscore(REDIS_KEY,proxy)
        if score and score>MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减1')
            return self.db.zincrby(REDIS_KEY,-1,proxy)
        else:
            print('代理',proxy,'当前分数',score,'移除')
            return self.db.zrem(REDIS_KEY,proxy)

    #定义一个方法判断代理是否存在
    def exists(self,proxy):
        return not self.db.zscore(REDIS_KEY,proxy)==None

    #定义一个方法设置代理分数为100
    def max(self,proxy):
        print('代理',proxy,'可用,设置为',MAX_SCORE)
        mapping={proxy:MAX_SCORE}
        return self.db.zadd(REDIS_KEY,mapping=mapping)

    #定义一个方法获取代理数量
    def count(self):
        return self.db.zcard(REDIS_KEY)

    #定义一个方法获取全部代理
    def all(self):
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

# if __name__ == '__main__':
#     proxy='103.141.4.110:8080'
#     print(RedisClient().all())
