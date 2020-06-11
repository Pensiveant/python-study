
from scrapy import cmdline
import sys
import os

dirpath = os.path.dirname(os.path.abspath(__file__))
print(os.path.abspath(__file__))
print(dirpath)
sys.path.append(dirpath)
os.chdir(dirpath)
cmdline.execute('scrapy crawl doubannewbook'.split())