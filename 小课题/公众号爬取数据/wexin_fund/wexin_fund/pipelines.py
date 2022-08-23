# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import csv
import pandas as pd
from pydispatch import dispatcher
from scrapy import signals

class WexinFundPipeline:
    def process_item(self, item, spider):
        return item


class SaveToCsvPipeline(object):
    def __init__(self):
        self.fundList = []
    def open_spider(self, spider):
        nowDate = datetime.datetime.now().strftime("%Y%m%d")
        filepath = '{}_股票型.csv'.format(nowDate)
        csvfile = open(filepath, 'w', encoding='utf-8-sig',
                       newline='')  # newline='' 解决空行问题
        self.csv_writer = csv.writer(csvfile)
        # 写入头部
        self.csv_writer.writerow(
            ['排名', '名称', '代码', '本周涨幅', '近一年', '近三年', '基金经理', '基金规模', '成立时间'])

    def process_item(self, item, spider):
        fundNew = [item['ranking'], item['name'], item['code'], item['weekGrowthRate'], item['oneYearGrowthRate'],
                                  item['threeYearGrowthRate'], item['fundManager'], item['scale'], item['establishDate']
                                  ]
        self.fundList.append(fundNew)
        # self.csv_writer.writerow([item['ranking'], item['name'], item['code'], item['weekGrowthRate'], item['oneYearGrowthRate'],
        #                           item['threeYearGrowthRate'], item['fundManager'], item['scale'], item['establishDate']
        #                           ])
        return item

    def close_spider(self, spider):
        self.fundList=sorted(self.fundList,key=(lambda x:x[0]))
        for item in self.fundList:
            self.csv_writer.writerow(item)
        

