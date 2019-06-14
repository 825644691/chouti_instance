#python连接数据库
#1pymysql
#2mysqldb ：不支持数据库

import pymysql


#创建连接
conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',passwd = '8256',db = 'dbnews')
#cursor = conn.cursor()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#可以取出列名，以字典的方式显示

# 数据库操作 - 增  -  (获取自增后的id)
# cursor.execute('insert into news(id,title,content)values(1,"嗄萨蒂","asd")')
inp = input("请输入id")
cursor.execute('insert into news(title,content)values(%s,%s)',(inp,inp))
conn.commit()
nid = cursor.lastrowid
print(nid)

# 数据库操作 - 增多条数据
# l = ((1111,"嗄萨蒂","asd"),
#      (2222,"嗄萨蒂","asd"),
#      (3333,"嗄萨蒂","asd"))
# cursor.executemany('insert into news(id,title,content)values(%s,%s,%s)',l)
# conn.commit()


#数据库操作 - 改
# r = cursor.execute('update news set title = %s where id =%s ', ('危机2',5))
# conn.commit()

#数据库操作 - 删
# d = cursor.execute('delete from news where id = %s' ,5)
# conn.commit()

#数据库操作 - 查
#fetchall拿到的是一个元组
#fetchone拿到的是一条数据
# q = cursor.execute('select * from news')
# print(q)
# result = cursor.fetchall() #fetchone /fetchtwo/fetchten只取一条数据
# for i in result:
#     print(i[0])
# print(result)
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# 数据库操作 - 查(手动移动指针)
# cursor.scroll(0,mode='absolute')
# cursor.scroll(-1,mode='relative')
# result = cursor.fetchone()
# print(result)



#数据库操作 - 查(错误操作)：黑客入侵-数据库注入
# sql = 'select id as i,title from news where title = "%s" and id = "%s"'
# sql = sql %('嗄萨蒂',1)
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)





