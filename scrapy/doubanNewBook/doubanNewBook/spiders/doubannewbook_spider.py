import scrapy
from bs4 import BeautifulSoup
from ..items import DoubannewbookItem

class doubanNewBook(scrapy.Spider):
    name = 'doubannewbook'
    start_urls = ['https://book.douban.com/latest?icn=index-latestbook-all']

    def parse(self, response):
        htmlText = response.text
        htmlDomTree = BeautifulSoup(htmlText, 'lxml')
        newBookItems=htmlDomTree.select('div.clearfix ul li')
        bookItems=DoubannewbookItem()
        for li in newBookItems:
            bookItems['name']=li.select('h2 a')[0].text.strip()
            bookItems['star']=li.select('p.rating span.color-lightgray')[0].text.strip()
            bookItems['author']=li.select('p.color-gray')[0].text.split('/')[0].strip()
            bookItems['publisher']=li.select('p.color-gray')[0].text.split('/')[1].strip()
            bookItems['publishTime']=li.select('p.color-gray')[0].text.split('/')[2].strip()
            bookItems['description']=li.select('p:last-child')[0].text.strip()
            yield bookItems

