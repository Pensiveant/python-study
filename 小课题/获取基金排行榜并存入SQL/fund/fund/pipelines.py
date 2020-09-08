# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import mysql.connector


class SaveToCsvPipeline(object):

    def open_spider(self, spider):
        csvfile = open(r'./fund.csv', 'w', encoding='utf-8-sig',newline='') # newline='' 解决空行问题
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


class SaveToMySQLPipeline(object):
    def __init__(self, mysqlConfig):
        self.mysqlConfig = mysqlConfig

    # 类方法，读取MySQL数据库配置
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mysqlConfig=crawler.settings.get('MYSQL_CONFIG'))

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(**self.mysqlConfig)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('INSERT INTO fundRanking (code, name, date, netAssetValue, accumulativeTotalTetValue, dailyGrowthRate, weekGrowthRate, oneMothGrowthRate, threeMothGrowthRate, sixMothGrowthRate, oneYearGrowthRate, twoYearGrowthRate,threeYearGrowthRate, nowYearGrowthRate, setUpGrowthRate,customGrowthRate, serviceChargeRate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            (item['code'], item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
                                  item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
                                  item['sixMothGrowthRate'], item['oneYearGrowthRate'], item[
                                      'twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
                                  item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']))
        self.conn.commit()

    def close_spider(self, item, spider):
        self.conn.close()  # 关闭连接
        yield item
