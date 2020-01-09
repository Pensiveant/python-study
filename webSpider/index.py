# 利用urllib简单抓取网页（https://blog.csdn.net/c406495762/article/details/58716886）

from urllib import request
import chardet

if __name__=='__main__':
    response=request.urlopen("https://www.baidu.com/")
    html=response.read()
    charset=charset.detect(html)
    html=html.decode(charset)
    print(html)

