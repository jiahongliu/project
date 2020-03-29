import requests
from DB.file import File_Storage
from hashlib import md5

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
}

class Got_Image():
    def __init__(self,url):
        self.url=url

    #获取网页图片或视频字节流
    def get_image(self):
        resp=requests.get(self.url,headers=headers)
        if resp.status_code==200:
            print('获取成功')
            return resp.content
        else:
            print('获取失败')
            print(resp.status_code)
            return None

    #定义一个方法保存图片
    def save_image(self,path):
        if self.get_image():
            print('保存图片中')
            content=self.get_image()
            md5_image=md5(content).hexdigest()+'.jpg'
            f=File_Storage(path=path,title='jjj',file=md5_image,content=content).storage_image()
            print('保存图片成功')
        else:
            print('失败')

    #定义一个方法保存视频
    def save_video(self,path):
        if self.get_image():
            print('保存视频中')
            content=self.get_image()
            md5_image=md5(content).hexdigest()+'.mp4'
            f=File_Storage(path=path,title='jjj',file=md5_image,content=content).storage_image()
            print('保存视频成功')
        else:
            print('失败')

if __name__ == '__main__':
    url='https://p5.ssl.qhimgs1.com/t01ee5b4bd1be957bff.jpg'
    path='G:\\fruit'
    f=Got_Image(url=url).save_image(path=path)