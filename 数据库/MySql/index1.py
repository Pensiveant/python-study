
'''
使用pymysql库访问mysql
'''
import pymysql


# 建立连接，host=127.0.0.1 port=3306
conn = pymysql.connect(user='root', password='mysql@123',database='share')
cursor = conn.cursor()
# 创建user表:
print('创建user表')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
# 关闭Cursor和Connection:
cursor.close()
conn.close()
