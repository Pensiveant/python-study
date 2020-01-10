'''
官方MySQL-Connector使用示例：删除数据
'''

import mysql.connector

# 连接数据库
cnx=mysql.connector.connect(user='root',password='mysql@123',database='share')
cursor=cnx.cursor()

# 删除id为1的数据
cursor.execute("DELETE FROM share WHERE id=1")
cnx.commit()

cursor.close()
cnx.close()