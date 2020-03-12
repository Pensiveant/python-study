# 获取网页的编码
# @author：pensiveant
# @reference：https://blog.csdn.net/c406495762/article/details/58716886
# @question: 百度首页的编码方式读取不正确

# -*- coding: UTF-8 -*-
from urllib import request
import chardet


def GetHtmlEcoding(url):
    response = request.urlopen(url)
    html = response.read()
    charset = chardet.detect(html)
    return charset['encoding']


# print(GetHtmlEcoding('https://www.baidu.com/'))
