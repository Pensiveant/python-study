# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import logging


class SaveToMySqlPipeline(object):

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
        self.cursor.execute('INSERT INTO doubannewbook (name,star,author,publisher,publishtime,description) VALUES (%s,%s,%s,%s,%s,%s)',
                            (item['name'], item['star'], item['author'], item['publisher'], item['publishTime'], item['description']))
        self.conn.commit()

    def close_spider(self, item, spider):
        self.conn.close()  # 关闭连接
        yield item
