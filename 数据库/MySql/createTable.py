'''
官方MySQL-Connector使用示例：创建表格
'''

import mysql.connector


# 创建基金排行榜表
cnx=mysql.connector.connect(user='root',password='mysql@123',database='fund')
cursor=cnx.cursor()

cursor.execute('CREATE TABLE fundRanking (code varchar(20) primary key, name varchar(20), date varchar(20), netAssetValue varchar(20), accumulativeTotalTetValue varchar(20), dailyGrowthRate varchar(20), weekGrowthRate varchar(20), oneMothGrowthRate varchar(20), threeMothGrowthRate varchar(20), sixMothGrowthRate varchar(20), oneYearGrowthRate varchar(20), twoYearGrowthRate varchar(20),threeYearGrowthRate varchar(20), nowYearGrowthRate varchar(20), setUpGrowthRate varchar(20),customGrowthRate varchar(20), serviceChargeRate varchar(20))')
cnx.commit()
cursor.close()
cnx.close()