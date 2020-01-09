'''
官方MySQL-Connector使用示例
'''

import mysql.connector

#cnx=mysql.connector.connect(user='root',password='mysql@123',database='share')
cnx=mysql.connector.MySQLConnection(user='root',password='mysql@123',database='share')
cursor=cnx.cursor()
# 创建表格
cursor.execute('create table share (id varchar(20) primary key, name varchar(20))')
# 插入一条数据
cursor.close()
cnx.close()