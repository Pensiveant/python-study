# -*- coding: utf-8 -*-
import scrapy
from ..items import SelectedFundItem


class FundspiderSpider(scrapy.Spider):
    name = 'fundSpider'
    requestParm = {
        'op': 'ph',
        'dt': 'kf',
        'ft': 'all',
        'rs': '',
        'gs': 0,
        'sc': 'jnzf',
        'st': 'desc',
        'sd': '2019-09-07',  # 自定义
        'ed': '2020-09-07',
        'qdii': '',
        'tabSubtype': ',,,,,',
        'pi': '1',  # pageIndex
        'pn': '500000',  # pageNumber
        'dx': '1',
        'v': '0.6265998610926615'
    }
    url = 'http://fund.eastmoney.com/data/rankhandler.aspx?' + \
        '&'.join([str(key)+'='+str(value)
                 for key, value in requestParm.items()])
    start_urls = [url]

    def format_rate(self, rate):
        return ('---' if rate == '' else '{}%'.format(rate))

    def parse(self, response):
        selecedFund = ['001809', '002420', '014191', '519212', '519191', '519185', '012148', '012149',
                       '007689', '007690', '720001', '000828', '004997', '002810', '004685', '001097',
                       '005598', '240004', '001678', '002910', '001832', '005669', '470021', '002296',
                       '002420', '000772', '162607','000690','001816','005290','002938','001475','002885','210002','006603']
        selecedFund = list(set(list(selecedFund)))
        data = response.text.split('{')[1].split('}')[
            0].split(':')[1].split('","')
        data[0] = data[0].replace('["', '')
        data[-1] = data[-1].replace('"]', '')
        fundItems = data
        fundItem = SelectedFundItem()
        for item in fundItems:
            code = item.split(',')[0]
            if code in selecedFund:
                fundItem['code'] = item.split(',')[0]
                fundItem['name'] = item.split(',')[1]
                fundItem['weekGrowthRate'] = self.format_rate(
                    item.split(',')[7])
                fundItem['oneMothGrowthRate'] = self.format_rate(
                    item.split(',')[8])
                fundItem['threeMothGrowthRate'] = self.format_rate(
                    item.split(',')[9])
                fundItem['sixMothGrowthRate'] = self.format_rate(
                    item.split(',')[10])
                fundItem['oneYearGrowthRate'] = self.format_rate(
                    item.split(',')[11])
                fundItem['twoYearGrowthRate'] = self.format_rate(
                    item.split(',')[12])
                fundItem['threeYearGrowthRate'] = self.format_rate(
                    item.split(',')[13])
                fundItem['nowYearGrowthRate'] = self.format_rate(
                    item.split(',')[14])
                fundItem['setUpGrowthRate'] = self.format_rate(
                    item.split(',')[15])
                yield fundItem
