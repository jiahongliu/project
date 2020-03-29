import pymongo

MONGO_HOST='localhost'
MONGO_PORT=27017
DB_NAME='jjj'
TABLE_NAME='hhh'

class MongoDB_Storage():
    def __init__(self):
        #创建连接
        self.client=pymongo.MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        #选择数据库
        self.db=self.client[DB_NAME]
        #选择表
        self.collection=self.db[TABLE_NAME]

    #定义一个方法插入数据
    def storage_mongo(self,dict_content):
        #如果传入的参数是字典类型
        if isinstance(dict_content,dict):
            self.collection.insert_one(dict_content)
            print('插入成功')
        #如果传入参数是列表
        elif isinstance(dict_content,list):
            self.collection.insert_many(dict_content)
            print('插入成功')
        else:
            print('插入失败')
    #定义一个方法查询数据
    def select_monge(self,conditions,num=True):
        if isinstance(conditions,dict):
            if not num:
                return self.collection.find_one(conditions)
            elif num:
                return self.collection.find(conditions)

    #定义一个方法返回数据数量
    def count(self,conditions=None):
        #如果没有条件就统计全部数量
        if not conditions:
            return self.collection.estimated_document_count()
        else:
            return self.collection.count_documents(conditions)

    #定义一个方法删除数据 num控制删除一条还是所有
    def dele(self,cond,num=True):
        #确认参数类型
        if isinstance(cond,dict):
            # num为1表示只删除一个符合条件的数据
            if not num :
                self.collection.delete_one(cond)
            else:
                return self.collection.delete_many(cond)

# if __name__ == '__main__':
#     a={'name':'郏哥哥'}
#     b=MongoDB_Storage().select_monge(a)
#     for i in b:
#         print(i)
