import urllib.request

# 使用urlopen和urlretrieve抓取网页


#urllib.request.urlopen(url,data,timeout):发起请求
#url:需要打开的网址
#data：访问url时候发送的数据包，默认为null
#timeout：等待时长（超时）

requestUrl='https://www.zhihu.com/'

# 方法1：
resp = urllib.request.urlopen(requestUrl)
# html编码格式在head标签的charset属性中
# decode():解码 把字节流形式的数据以相应的格式转换为字符串。
print(resp.read().decode('utf-8'))


# 第二种方法


# filename=urllib.request.urlretrieve(requestUrl,filename='zhihu.html')
# # 这种方法会在电脑中产生缓存，占用资源，需清除缓存。
# urllib.request.urlcleanup()