from urllib import request


# 
keyword=input('请输入你想搜索的关键词：')
# 处理中文
key=request.quote(keyword)
url='http://www.baidu.com/s?wd='+key
req=request.urlopen(url)
result=req.read()
fl=open('baidu.html','wb')
fl.write(result)
fl.close()