# 获取百度翻译的html
# @author：pensiveant
# @reference：https://blog.csdn.net/c406495762/article/details/58716886

# -*- coding: UTF-8 -*-
from urllib import request
import chardet
from testEcoding import GetHtmlEcoding

baiduUrl='https://fanyi.baidu.com/#auto/zh/'
charact=GetHtmlEcoding(baiduUrl)
response=request.urlopen(baiduUrl)
html=response.read()
html=html.decode(charact)
print(html)





