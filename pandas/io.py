import pandas as pd
import os


# 读取CSV
dir = os.path.dirname(__file__)  # 当前.py文件所在目录
csvData = pd.read_csv(f'{dir}/20220920_自选.csv')
print(csvData)


# 读取json
jsonData = pd.read_json(f'{dir}/test.json')
print(jsonData)
