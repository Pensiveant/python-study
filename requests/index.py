import requests
import csv

year=input('输入年份:')
r=input('input r:')
condition={
    'max':10,
    'type':'c',
    'freq':'A',
    'px':'HS',
    'ps':year,
    'r':r,
    'p':0,
    'rg':2,
    'cc':'AG6',
    'uitoken':'19774f13ca46af6f08d0975e91ec9cd3'
}
r=requests.get('https://comtrade.un.org/api/get',condition)

if r.status_code==200:
    response=r.json()
else:
    print('请求失败')


# 写到CSV中
data=response['dataset']
csvfile=open('test.csv','w',newline='')
writer = csv.writer(csvfile)
keys=data[0].keys()
writer.writerow(tuple(keys))

csvData=[]
for item in data:
    csvData.append(item.values())
writer.writerows(csvData)
csvfile.close()
