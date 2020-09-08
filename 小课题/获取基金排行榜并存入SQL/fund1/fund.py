import requests

url = 'http://fund.eastmoney.com/data/rankhandler.aspx'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Referer':'http://fund.eastmoney.com/data/fundranking.html'
}
requestParm = {
    'op': 'ph',
    'dt': 'kf',
    'ft': 'all',
    'rs': '',
    'gs': 0,
    'sc': 'zzf',
    'st': 'desc',
    'sd': '2019-09-07',
    'ed': '2020-09-07',
    'qdii': '',
    'tabSubtype': ',,,,,',
    'pi': '1',
    'pn': '50',
    'dx': '1',
    'v': '0.6265998610926615'
}
req = requests.get(url=url, params=requestParm, headers=headers)
req.encoding = 'utf-8'
html = req.text
print(html)
