'''
接口模块
'''

from flask import Flask,g
from db import RedisClient

__all__=['app']
app=Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis=RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'

@app.route('/random')
#获取代理
def get_proxy():
    coon=get_conn()
    return coon.random()

@app.route('/count')
#获取代理数量
def get_counts():
    conn=get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run()