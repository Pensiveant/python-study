# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import csv


class SelectedFundPipeline:
    def process_item(self, item, spider):
        return item


class SaveToCsvPipeline(object):

    def __init__(self):
        self.fundList = []

    def open_spider(self, spider):
        nowDate = datetime.datetime.now()
        nowDateStr = (nowDate).strftime("%Y%m%d")
        filepath = '{}_自选.csv'.format(nowDateStr)
        csvfile = open(filepath, 'w', encoding='utf-8-sig',
                       newline='')  # newline='' 解决空行问题
        self.csv_writer = csv.writer(csvfile)
        # 写入头部
        self.csv_writer.writerow(
            ['基金名称', '基金代码', '近一周', '近一个月', '近三个月', '近六个月', '近一年', '近两年', '近三年', '今年来', '成立来',
             ])

    def process_item(self, item, spider):

        fundNew = [item['name'], item['code'], item['weekGrowthRate'], item['oneMothGrowthRate'],
                   item['threeMothGrowthRate'], item['sixMothGrowthRate'], item['oneYearGrowthRate'], item['twoYearGrowthRate'],
                   item['threeYearGrowthRate'], item['nowYearGrowthRate'], item['setUpGrowthRate']]
        self.fundList.append(fundNew)
        return item

    def close_spider(self, spider):
        # self.fundList = sorted(self.fundList, key=(lambda x: x[1]))
        for item in self.fundList:
            self.csv_writer.writerow(item)
