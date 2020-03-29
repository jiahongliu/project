import pymysql
MYSQL_HOST='localhost'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASS='jjjj'
MYSQL_DB='emt'

class Mysql_Storage():
    def __init__(self):
        #连接数据库数据表
        self.db=pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB, charset='utf8')
        #获取Mysql的操作游标
        self.cur=self.db.cursor()

    #定义方法插入数据 传入一个字典
    def storage_mysql(self, table_a, data_a):
        keys = ','.join(data_a.keys())
        values = ','.join(['%s'] * len(data_a))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table_a, keys=keys, values=values)
        try:
            self.cur.execute(sql, tuple(data_a.values()))
            self.db.commit()
            print('成功')
        except:
            print('失败')
            self.db.rollback()

        self.db.close()

    #定义一个方法更新数据 存在就更新不存在就插入
    def update_mysql(self,table,data):
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) values ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values)
        update = ','.join([' {key}=%s'.format(key=key) for key in data])
        sql += update
        try:
            self.cur.execute(sql, tuple(data.values()) * 2)
            self.db.commit()
            print('成功')
        except:
            print('失败')
            self.db.rollback()
        self.db.close()

    #定义一个方法删除数据
    def dete(self,table,condition):
        sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
        try:
            self.cur.execute(sql)
            self.db.commit()
            print('成功')
        except:
            print('失败')
            self.db.rollback()
        self.db.close()

    #定义一个方法查询数据
    def select(self,table,condition):
        sql = 'SELECT * FROM {table} WHERE {condition}'.format(table=table, condition=condition)
        try:
            self.cur.execute(sql)
            self.db.commit()
            for row in self.cur:
                print(row)
        except:
            print('失败')
            self.db.rollback()
        self.db.close()



# if __name__ == '__main__':
#     table = 'emp'
#
#     data = {
#         'id':2,
#         'name': 'yyj',
#         'salary': 200,
#         'DepartmentId': 2,
#     }
#     condition='name="yyj"'
#     a=Mysql_Storage().select(table=table,condition=condition)