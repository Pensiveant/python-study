from bs4 import BeautifulSoup
import requests

w3schoolUrl='https://www.w3school.com.cn/html/index.asp'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
w3schoolRequest=requests.get(w3schoolUrl,headers=headers)
w3schoolRequest.encoding='gbk'
w3schoolHtml=w3schoolRequest.text
w3schoolDomTree=BeautifulSoup(w3schoolHtml,'lxml')
wrapperDiv=w3schoolDomTree.body.div

# 使用.contents and .children属性
child=wrapperDiv.contents
for childDiv in wrapperDiv.children:
    print(childDiv)
