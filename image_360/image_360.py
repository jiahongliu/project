import requests
import json
from gotter.got_image import Got_Image
from queue import Queue
from threading import Thread
import aiohttp
import asyncio

#控制线程数量
Num=5
#控制图片存储地址
path='G:\\fruit'
#控制爬取页数
page=10
#请求头
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
}


class Image_360():
    def __init__(self):
        self.image_urls=[]

    # 生产url
    def producter(self):
        urls = []
        for i in range(page):
            urls.append('https://image.so.com/zjl?ch=wallpaper&sn=' + str(i * 30) + '&pn=30')
        return urls

    # 获取图片对应的gid的方法
    def get_gid(self,urls=None):
        gids = []
        if urls:
            if isinstance(urls, list):
                for url in urls:
                    resp = requests.get(url, headers=headers).text
                    js_str = json.loads(resp)['list']
                    for js in js_str:
                        gids.append(js['grpmd5'])
        return gids

    # 异步获取图片url
    async def get_images_url(self,url):
        async with aiohttp.ClientSession() as s:
            async with await s.get(url, headers=headers) as resp:
                page_text = await resp.text()
                return page_text

    # 回调函数将url存入列表中
    def callback(self,task):
        data = task.result()
        js_str = json.loads(data)['result']
        for image_url in js_str:
            self.image_urls.append(image_url['qhimg_url'])

    #协程
    def coroutines(self):
        urls = self.producter()
        print('urls采集完成')
        gids = self.get_gid(urls)
        print('gits采集完成')
        tasks = []
        for gid in gids:
            url = 'https://image.so.com/z?a=jsondetailbygidv2&identity=list&ch=wallpaper&gid=' + gid
            c = self.get_images_url(url)
            task = asyncio.ensure_future(c)
            task.add_done_callback(self.callback)
            tasks.append(task)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))

    #调用自己设计的保存图片方法
    def save(self,in_q):
        while in_q.empty() is not True:  # 队列不为空
            Got_Image(in_q.get()).save_image(path=path)
            in_q.task_done()

    def run(self):
        # 协程获取了图片地址
        self.coroutines()
        q = Queue()
        for url in self.image_urls:
            q.put(url)
        print('初始数量:%s' % q.qsize())

        for index in range(Num):
            thread = Thread(target=self.save, args=(q,))
            thread.daemon = True
            thread.start()
        q.join()

if __name__ == '__main__':
    Image_360().run()






