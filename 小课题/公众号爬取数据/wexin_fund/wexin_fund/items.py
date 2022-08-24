# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WexinFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type=scrapy.Field() # 基金类型
    ranking=scrapy.Field() # 排名
    name=scrapy.Field() # 基金名称
    code=scrapy.Field() # 基金code
    weekGrowthRate=scrapy.Field() # 近一周增长率
    oneYearGrowthRate=scrapy.Field() # 近一年增长率
    threeYearGrowthRate=scrapy.Field() # 近三年增长率
    fundManager=scrapy.Field() # 基金经理
    scale=scrapy.Field() # 基金规模
    establishDate=scrapy.Field() # 成立时间
    pass
