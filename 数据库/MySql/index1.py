'''
官方MySQL-Connector使用示例：插入数据
'''

import mysql.connector

# 连接数据库
cnx=mysql.connector.connect(user='root',password='mysql@123',database='share')
cursor=cnx.cursor()

# 插入一条数据
cursor.execute('INSERT INTO SHARE (id,name) VALUES (%s,%s)',(1,'pensiveant'))
cnx.commit()

# 插入多条数据
rows=[(2,'zhangshan'),(3,'李四')]
cursor.executemany('INSERT INTO SHARE (id,name) VALUES (%s,%s)',rows)
cnx.commit()

cursor.close()
cnx.close()