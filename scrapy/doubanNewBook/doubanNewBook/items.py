# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubannewbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field() # 书名
    star=scrapy.Field() # 评分
    author=scrapy.Field() # 作者
    publisher=scrapy.Field() # 出版社
    publishTime=scrapy.Field() # 出版时间
    description=scrapy.Field() # 描述
