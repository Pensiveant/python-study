# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SelectedFundItem(scrapy.Item):
    name=scrapy.Field() # 基金名称
    code=scrapy.Field() # 基金代码   
    weekGrowthRate=scrapy.Field() # 近一周增长率
    oneMothGrowthRate=scrapy.Field() # 近一个月增长率
    threeMothGrowthRate=scrapy.Field() # 近三个月增长率
    sixMothGrowthRate=scrapy.Field() # 近六个月增长率
    oneYearGrowthRate=scrapy.Field() # 近一年增长率
    twoYearGrowthRate=scrapy.Field() # 近两年增长率
    threeYearGrowthRate=scrapy.Field() # 近三年增长率
    nowYearGrowthRate=scrapy.Field() # 今年以来增长率
    setUpGrowthRate=scrapy.Field() # 成立以来增长率
    pass