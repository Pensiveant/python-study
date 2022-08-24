# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import WexinFundItem
import json
import datetime
from bs4 import BeautifulSoup


class FundspiderSpider(scrapy.Spider):
    name = 'fundSpider'

    def start_requests(self):
        nowDate = datetime.datetime.now()
        filenames = {
            'gp': '股票型',
            'hh': '混合型',
            'zs': '指数型',
            'qdii': 'QDII'
        }
        self.fundTypeName = filenames[self.type]
        requestParm = {
            'op': 'ph',
            'dt': 'kf',
            # 基金类型（'all':全部，'gp':股票型，'hh':混合型,'zq':债券型,'zs':指数型，'qdii'：QDII，'lof':LOF，'fof':FOF）
            'ft': self.type,
            'rs': '',
            'gs': 0,
            # 排序类型（'rzdf':日增长率，'zzf':近1周，'1yzf':近一月，'3yzf':近三月，'6yzf':近六月，'1nzf':近一年，
            #          '2nzf':近两年,'3nzf':近三年,'jnzf':今年来,'lnzf':成立以来）
            'sc': 'zzf',
            'st': 'desc',  # 升序还是降序（'desc':降序,'asc':升序）
            # 开始日期
            'sd': '{}-{}-{}'.format(nowDate.year, nowDate.month, nowDate.day),
            # 结束日期
            'ed': '{}-{}-{}'.format(nowDate.year, nowDate.month, nowDate.day),
            'qdii': '',
            'tabSubtype': ',,,,,',
            'pi': '1',  # pageIndex
            'pn': '10',  # pageNumber
            'dx': '1',
            'v': '0.6265998610926615'
        }
        url = 'http://fund.eastmoney.com/data/rankhandler.aspx?' + \
            '&'.join([str(key)+'='+str(value)
                      for key, value in requestParm.items()])
        yield scrapy.Request(url)
        
    def parseFund(self, response):
        meta = response.meta
        fundItem = WexinFundItem()
        fundItem['type'] = self.fundTypeName
        fundItem['ranking'] = meta['ranking']
        fundItem['name'] = meta['name']
        fundItem['code'] = meta['code']
        fundItem['weekGrowthRate'] = (
            '---' if meta['weekGrowthRate'] == '' else '{}%'.format(meta['weekGrowthRate']))
        fundItem['oneYearGrowthRate'] = (
            '---' if meta['oneYearGrowthRate'] == '' else '{}%'.format(meta['oneYearGrowthRate']))
        fundItem['threeYearGrowthRate'] = (
            '---' if meta['threeYearGrowthRate'] == '' else '{}%'.format(meta['threeYearGrowthRate']))
        #
        fundHtml = response.text
        fundDomTree = BeautifulSoup(fundHtml, 'lxml')
        scaleDom = fundDomTree.select(
            '.fundInfoItem .infoOfFund table tr:nth-child(1) td:nth-child(2)')
        fundItem['scale'] = scaleDom[0].get_text().split('：')[1]
        managerDom = fundDomTree.select(
            '.fundInfoItem .infoOfFund table tr:nth-child(1) td:nth-child(3)')
        fundItem['fundManager'] = managerDom[0].get_text().split('：')[1]
        establishDateDom = fundDomTree.select(
            '.fundInfoItem .infoOfFund table tr:nth-child(2) td:nth-child(1)')
        fundItem['establishDate'] = establishDateDom[0].get_text().split('：')[
            1]
        yield fundItem

    def parse(self, response):
        data = response.text.split('{')[1].split('}')[
            0].split(':')[1].split('","')
        data[0] = data[0].replace('["', '')
        data[-1] = data[-1].replace('"]', '')
        fundItems = data
        for index, item in enumerate(fundItems):
            ranking = index+1
            code = item.split(',')[0]
            name = item.split(',')[1]
            weekGrowthRate = item.split(',')[7]
            oneYearGrowthRate = item.split(',')[11]
            twoYearGrowthRate = item.split(',')[12]
            threeYearGrowthRate = item.split(',')[13]
            itemUrl = 'http://fund.eastmoney.com/{}.html'.format(code)
            yield scrapy.Request(url=itemUrl, callback=self.parseFund, meta={"ranking": ranking, "code": code, "name": name, "weekGrowthRate": weekGrowthRate, "oneYearGrowthRate": oneYearGrowthRate, "twoYearGrowthRate": twoYearGrowthRate, "threeYearGrowthRate": threeYearGrowthRate})
