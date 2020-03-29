'''
调度模块
'''

TESTER_CYCLE=20
GETTER_CYCLE=20
TESTER_ENDBLED=True
GETTER_ENDBLED=True
API_ENDBLED=True

from multiprocessing import Process
from api import app
from getter import Getter
import time
from tester import Tester

class Scheduler():
    def schedule_tester(self,cycle=TESTER_CYCLE):
        tester=Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        getter=Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        app.run('127.0.0.1','5000')

    def run(self):
        print('代理池开始执行')
        if TESTER_ENDBLED:
            tester_process=Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENDBLED:
            getter_process=Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENDBLED:
            api_process=Process(target=self.schedule_api)
            api_process.start()