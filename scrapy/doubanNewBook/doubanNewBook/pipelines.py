# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import logging


class DoubannewbookPipeline(object):
    def open_spider(self, spider):
        config = {
            'user': 'root',
                    'password': 'mysql@123',
                    'host': '127.0.0.1',
                    'database': 'scrapy',
                    'raise_on_warnings': True
        }
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('INSERT INTO doubannewbook (name,star,author,publisher,publishtime,description) VALUES (%s,%s,%s,%s,%s,%s)',(item['name'], item['star'], item['author'], item['publisher'], item['publishTime'], item['description']))
        self.conn.commit()
       
    def close_spider(self,item, spider):
        self.conn.close()  # 关闭连接
        yield item
