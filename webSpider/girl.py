# 爬取妹子图网的图片
# @Time:20200310

# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import urllib
from urllib import request
import os
import time
import re

if __name__ == '__main__':
    list_url = []
    for num in range(1, 20):
        if num == 1:
            url = 'https://www.mzitu.com/'
        else:
            url = 'https://www.mzitu.com/tag/ugirls/page/{0}/'.format(num)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.select('#pins li > a')
        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print('连接采集完成')

    # 使用IP代理
    def useIpAgent():
        proxy = {'http': '106.46.136.112:808'}
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        opener.addheaders = [
            ("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36')]
        request.install_opener(opener)
    # 下载图片

    def down_pic(url, path):
        try:
            req = request.Request(url)
            data = request.urlopen(req).read()
            with open(path, 'wb') as f:
                f.write(data)
                f.close()
        except Exception as e:
            print(str(e))
    for each_img in list_url:
        img_info = each_img.split('=')
        target_url = img_info[1]
        filename = img_info[0] + '.jpg'
        print('下载：' + filename)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        img_req = requests.get(url=target_url, headers=headers)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf_1 = BeautifulSoup(img_html, 'lxml')

        imgObj = img_bf_1.select_one('.main-image img')
        img_url = imgObj.get('src')
        if 'girlImages' not in os.listdir(r'D:\pensiveant\github\python-study\webSpider'):
            os.makedirs(r'./webSpider/girlImages')

        work_path = os.path.join(
            'D:\pensiveant\github\python-study\webSpider\girlImages', filename)
        opener = urllib.request.build_opener()
        refererNumber =  re.sub("\D", "", target_url)
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'),
            ('Referer', 'https://www.mzitu.com/'+refererNumber)]
        urllib.request.install_opener(opener)
        # useIpAgent()
        urlretrieve(url=img_url, filename=work_path)
        # down_pic(img_url,work_path)
    print('下载完成！')
