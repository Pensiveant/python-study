'''
官方MySQL-Connector使用示例：创建表格
'''

import mysql.connector


cnx=mysql.connector.connect(user='root',password='mysql@123',database='share')
cursor=cnx.cursor()

# 创建表格test
cursor.execute('CREATE TABLE test (id varchar(20) primary key, name varchar(20))')
cnx.commit()

cursor.close()
cnx.close()