# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import mysql.connector
from twisted.enterprise import adbapi


class SaveToCsvPipeline(object):

    def open_spider(self, spider):
        csvfile = open(r'./fund.csv', 'w', encoding='utf-8-sig',
                       newline='')  # newline='' 解决空行问题
        self.csv_writer = csv.writer(csvfile)
        # 写入头部
        self.csv_writer.writerow(
            ['code', 'name', 'date', 'netAssetValue', 'accumulativeTotalTetValue', 'dailyGrowthRate', 'weekGrowthRate', 'oneMothGrowthRate', 'threeMothGrowthRate', 'sixMothGrowthRate', 'oneYearGrowthRate', 'twoYearGrowthRate', 'threeYearGrowthRate', 'nowYearGrowthRate', 'setUpGrowthRate',
             'customGrowthRate', 'serviceChargeRate'])

    def process_item(self, item, spider):

        self.csv_writer.writerow([item['code']+'\t', item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
                                  item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
                                  item['sixMothGrowthRate'], item['oneYearGrowthRate'], item[
                                      'twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
                                  item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']])

    def close_spider(self, item, spider):
        yield item

# 同步，事务加批量写入
# 参考：https://www.jb51.net/article/133144.htm


class SaveToMySQLPipeline(object):
    def __init__(self, mysqlConfig):
        self.mysqlConfig = mysqlConfig
        self.items = []

    # 类方法，读取MySQL数据库配置
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mysqlConfig=crawler.settings.get('MYSQL_CONFIG'))

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(**self.mysqlConfig)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.items.append((item['code'], item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
                           item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
                           item['sixMothGrowthRate'], item['oneYearGrowthRate'], item[
            'twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
            item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']))

        # self.cursor.execute('INSERT INTO fundRanking (code, name, date, netAssetValue, accumulativeTotalTetValue, dailyGrowthRate, weekGrowthRate, oneMothGrowthRate, threeMothGrowthRate, sixMothGrowthRate, oneYearGrowthRate, twoYearGrowthRate,threeYearGrowthRate, nowYearGrowthRate, setUpGrowthRate,customGrowthRate, serviceChargeRate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        #                     (item['code'], item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
        #                      item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
        #                      item['sixMothGrowthRate'], item['oneYearGrowthRate'], item[
        #                         'twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
        #                      item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']))
        # self.conn.commit()
        return item

    def close_spider(self, spider):
        insert_sql = """
         INSERT INTO fundRanking (code, name, date, netAssetValue, accumulativeTotalTetValue, dailyGrowthRate, weekGrowthRate, oneMothGrowthRate, threeMothGrowthRate, sixMothGrowthRate, oneYearGrowthRate, twoYearGrowthRate,threeYearGrowthRate, nowYearGrowthRate, setUpGrowthRate,customGrowthRate, serviceChargeRate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        insertItems = [self.items[i:i+20]
                       for i in range(0, len(self.items), 20)]
        transactionItems = [insertItems[i:i+20]
                            for i in range(0, len(insertItems), 20)]
        for item in transactionItems:
            self.conn.start_transaction()
            for index in range(len(item)):
                self.cursor.executemany(insert_sql, tuple(item[index]))
            self.conn.commit()
        self.conn.close()  # 关闭连接


# 参考：https://blog.csdn.net/loner_fang/article/details/81056191
class AsynSaveToMySQLPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool(
            'mysql.connector', **settings['MYSQL_CONFIG'])
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
       INSERT INTO fundRanking (code, name, date, netAssetValue, accumulativeTotalTetValue, dailyGrowthRate, weekGrowthRate, oneMothGrowthRate, threeMothGrowthRate, sixMothGrowthRate, oneYearGrowthRate, twoYearGrowthRate,threeYearGrowthRate, nowYearGrowthRate, setUpGrowthRate,customGrowthRate, serviceChargeRate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        cursor.execute(insert_sql, (item['code'], item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
                                    item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
                                    item['sixMothGrowthRate'], item['oneYearGrowthRate'], item[
            'twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
            item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)
