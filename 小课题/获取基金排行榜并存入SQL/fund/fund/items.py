# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code=scrapy.Field() # 基金代码
    name=scrapy.Field() # 基金名称
    date=scrapy.Field() # 日期
    netAssetValue=scrapy.Field() # 单位净值
    accumulativeTotalTetValue=scrapy.Field() # 累计净值
    dailyGrowthRate=scrapy.Field() # 日增长率
    weekGrowthRate=scrapy.Field() # 近一周增长率
    oneMothGrowthRate=scrapy.Field() # 近一个月增长率
    threeMothGrowthRate=scrapy.Field() # 近三个月增长率
    sixMothGrowthRate=scrapy.Field() # 近六个月增长率
    oneYearGrowthRate=scrapy.Field() # 近一年增长率
    twoYearGrowthRate=scrapy.Field() # 近两年增长率
    threeYearGrowthRate=scrapy.Field() # 近三年增长率
    nowYearGrowthRate=scrapy.Field() # 今年以来增长率
    setUpGrowthRate=scrapy.Field() # 成立以来增长率
    customGrowthRate=scrapy.Field() # 自定义增长率(当前日期向前推一年)
    serviceChargeRate=scrapy.Field() # 手续费
