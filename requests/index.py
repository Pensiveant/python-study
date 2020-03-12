import requests
from bs4 import BeautifulSoup

requestUrl='https://www.pexels.com/zh-cn/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
request=requests.get(requestUrl,headers=headers)
request.encoding='utf-8'
html=request.text
bf=BeautifulSoup(html,'lxml')
divTag=bf.find_all('div')
print(bf.prettify())