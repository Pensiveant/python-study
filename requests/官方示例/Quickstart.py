import requests

# get请求
response=requests.get('https://api.github.com/events')

# post请求

response=requests.post('https://httpbin.org/post', data = {'key':'value'})

print('---')