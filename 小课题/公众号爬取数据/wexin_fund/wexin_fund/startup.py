
from scrapy import cmdline
import sys
import os

dirpath = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(dirpath)
sys.path.append(dirpath)
os.chdir(dirpath)
# cmdline.execute('scrapy crawl fundSpider -a type=gp'.split()) # 股票型
# cmdline.execute('scrapy crawl fundSpider -a type=hh'.split()) # 混合型
# cmdline.execute('scrapy crawl fundSpider -a type=zs'.split()) # 指数型
# cmdline.execute('scrapy crawl fundSpider -a type=qdii'.split()) # QDII

# 
os.system('scrapy crawl fundSpider -a type=gp') 
os.system('scrapy crawl fundSpider -a type=hh') 
os.system('scrapy crawl fundSpider -a type=zs') 
os.system('scrapy crawl fundSpider -a type=qdii') 