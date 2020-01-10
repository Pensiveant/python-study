'''
官方MySQL-Connector使用示例：查询数据
'''

import mysql.connector

# 连接数据库
cnx=mysql.connector.connect(user='root',password='mysql@123',database='share')
cursor=cnx.cursor()

# 列信息
print(cursor.column_names)

# 获取所有数据(fetchone())
cursor.execute("SELECT * FROM share")
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()

# 获取所有数据（fetchall()）
cursor.execute("SELECT * FROM share")
rows=cursor.fetchall()
print(rows)

cursor.close()
cnx.close()