import numpy as np
import pandas as pd

# 本示例为如何查看数据
# @author:pensiveant
# @reference:https://www.pypandas.cn/docs/getting_started/10min.html#%E6%9F%A5%E7%9C%8B%E6%95%B0%E6%8D%AE

dates=pd.date_range('20200304',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

# 查看DataFrame头部和尾部的数据
head=df.head()
# print(head)
tail=df.tail(3)
# print(tail)


# 显示索引和列名
index=df.index
# print(index)
columns=df.columns
# print(columns)

# 输出底层的NumPy对象
numPy=df.to_numpy()
# print(numPy)

# 查看数据的统计概要
describe=df.describe()
# print(describe)

# 转置数据
t=df.T
# print(t)

# 按轴排序
sort=df.sort_index(axis=1,ascending=False)
# print(sort)

# 按值排序
value=df.sort_values(by='B')
print(value)