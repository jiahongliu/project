from db import RedisClient
from get_proxy import Got_Proxie

#设置代理池数量上限
POOL_UPPER_THRESHOLD=1000

class Getter():
    def __init__(self):
        self.redis=RedisClient()
        self.got_proxie=Got_Proxie()

    #判断代理数量是否达到限值
    def is_threshold(self):
        if self.redis.count()>=POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('执行开始')
        #如果代理数量没有达到限值
        if not self.is_threshold():
            proxies=self.got_proxie.got_proxie_ip66()
            for proxy in proxies:
                self.redis.add(proxy)

if __name__ == '__main__':
    Getter().run()
