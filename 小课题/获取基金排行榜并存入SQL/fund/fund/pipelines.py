# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class SaveToCsvPipeline(object):

    def open_spider(self, spider):
        csvfile = open(r'./fund.csv', 'w', encoding='utf-8-sig')
        self.csv_writer = csv.writer(csvfile)
        self.csv_writer.writerow(
            ['code', 'name', 'date', 'netAssetValue', 'accumulativeTotalTetValue', 'dailyGrowthRate', 'weekGrowthRate', 'oneMothGrowthRate'
            , 'threeMothGrowthRate','sixMothGrowthRate','oneYearGrowthRate','twoYearGrowthRate','threeYearGrowthRate','nowYearGrowthRate','setUpGrowthRate',
            'customGrowthRate','serviceChargeRate'])

    def process_item(self, item, spider):

        self.csv_writer.writerow([item['code']+'\t', item['name'], item['date'], item['netAssetValue'], item['accumulativeTotalTetValue'],
                                  item['dailyGrowthRate'], item['weekGrowthRate'], item['oneMothGrowthRate'], item['threeMothGrowthRate'],
                                  item['sixMothGrowthRate'], item['oneYearGrowthRate'],item['twoYearGrowthRate'], item['threeYearGrowthRate'], item['nowYearGrowthRate'],
                                  item['setUpGrowthRate'], item['customGrowthRate'], item['serviceChargeRate']])

    def close_spider(self, item, spider):
        yield item
