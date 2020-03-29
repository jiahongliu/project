import os

class File_Storage():
    def __init__(self,path,title,file,content):
        self.path=path+'\\'+title
        self.file=file
        self.content=content

    #定义一个创建文件的方法
    def create_folder(self):
        if not os.path.exists(self.path):  # 若文件夹不存在则新建
            os.makedirs(self.path)

    #定义一个存储文本方法
    def storage_file(self):
        new_path=self.path+'\\'+self.file
        with open(new_path,'w',encoding='utf-8') as f:
            f.write(self.content)
            f.close()

    #定义一个存储图片方法
    def storage_image(self):
        new_path = self.path + '\\' + self.file
        with open(new_path, 'wb') as f:
            f.write(self.content)
            f.close()

    #定义一个启动方法
    def run(self):
        print('存储开始')
        self.create_folder()
        self.storage_file()
        print('存储成功')

if __name__ == '__main__':
    path='G:\\fruit'
    title='jhl'
    file='jhl.txt'
    content='hhh'
    jhl=File_Storage(path,title,file,content).run()



