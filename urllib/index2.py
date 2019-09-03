from urllib import request
from urllib import parse


url='http://github.com/login'

#urlencode():将上传的数据进行编码处理
#encode():将字符串转换为相应编码格式的字节流数据
postData=parse.urlencode({
    'login':'Pensiveant',
    'password':'github@123'
}).encode('utf-8')

# 发送请求
req=request.urlopen(url,data=postData).read()

fl=open('github.html','wb')
fl.write(req)
fl.close()
