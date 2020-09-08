# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import FundItem
import json

class FundspiderSpider(scrapy.Spider):
    name = 'fundSpider'
    requestParm = {
        'op': 'ph',
        'dt': 'kf',
        'ft': 'all',
        'rs': '',
        'gs': 0,
        'sc': 'zzf',
        'st': 'desc',
        'sd': '2019-09-07', # 自定义
        'ed': '2020-09-07', # 
        'qdii': '',
        'tabSubtype': ',,,,,',
        'pi': '1',  # pageIndex
        'pn': '500000',  # pageNumber
        'dx': '1',
        'v': '0.6265998610926615'
    }
    url ='http://fund.eastmoney.com/data/rankhandler.aspx?'+ '&'.join([str(key)+'='+str(value) for key, value in requestParm.items()])
    start_urls = [url]

    def parse(self, response):
        data = response.text.split('{')[1].split('}')[0].split(':')[1].split('","')
        data[0]=data[0].replace('["','')
        data[-1]=data[-1].replace('"]','')
        fundItems =  data
        fundItem = FundItem()
        for item in fundItems:
            fundItem['code'] = item.split(',')[0]
            fundItem['name'] = item.split(',')[1]
            fundItem['date'] = item.split(',')[3]
            fundItem['netAssetValue'] = item.split(',')[4]
            fundItem['accumulativeTotalTetValue'] = item.split(',')[5]
            fundItem['dailyGrowthRate'] = item.split(',')[6]
            fundItem['weekGrowthRate'] = item.split(',')[7]
            fundItem['oneMothGrowthRate'] = item.split(',')[8]
            fundItem['threeMothGrowthRate'] = item.split(',')[9]
            fundItem['sixMothGrowthRate'] = item.split(',')[10]
            fundItem['oneYearGrowthRate'] = item.split(',')[11]
            fundItem['twoYearGrowthRate'] = item.split(',')[12]
            fundItem['threeYearGrowthRate'] = item.split(',')[13]
            fundItem['nowYearGrowthRate'] = item.split(',')[14]
            fundItem['setUpGrowthRate'] = item.split(',')[15]
            fundItem['customGrowthRate'] = item.split(',')[18]
            fundItem['serviceChargeRate'] = item.split(',')[20]
            yield fundItem
