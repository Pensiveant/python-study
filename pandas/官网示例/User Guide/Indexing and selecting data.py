'''
# Series和DataFrame索引示例
# @author:pensiveant
# @reference:https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#basics
'''

import pandas as pd
import numpy as np

# -------Basics----------------

# dates=pd.date_range('1/1/2000',periods=8)
# df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
# print(df)

# # 基础示例
# s=df['A']
# print(s)
# print(s[dates[5]])

# # 可以向[]中传入列表，按该顺序选取列
# df[['B', 'A']] = df[['A', 'B']] # 交换AB列
# print(df)

# # 注意：当使用.loc和.iloc时，将默认对齐轴。
# df.loc[:, ['B', 'A']] = df[['A', 'B']] # 无法交换
# df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy() # 交换AB列


# # ------Attribute access---------

# sa=pd.Series([1,2,3],index=list('abc'))
# dfa=df.copy()
# print(sa.b)
# print(dfa.A)

# # -----------Slicing ranges---------------

# # Series

# print(s)
# print(s[:5])
# print(s[::2]) # [开始：结束：步长]
# print(s[::-1]) # 当step等于负数的时候，从右向左取数。

# s2 = s.copy()
# s2[:5] = 0 # 也可以进行赋值
# print(s2)

# # DataFrame
# print(df[:3])
# print(df[::-1])

# -----------Selection by label-------------------

# # Series
# s1=pd.Series(np.random.randn(6),index=list('abcdef'))
# print(s1)
# print(s1.loc['c':]) # 获取标签'c'到末尾的切片
# print(s1.loc['b'])

# # DataFrame
# df1=pd.DataFrame(np.random.randn(6,4),index=list('abcdef'),columns=list('ABCD'))
# print(df1)
# print(df1.loc[['a','b','c'],:])
# print(df1.loc['d':,'A':'C'])
# print(df1.loc['a']) # a行
# print(df1.loc[:,df1.loc['a']>0]) # a行大于0的列

# ---------------Selection by position--------------

# # Series
# s1=pd.Series(np.random.randn(5),index=list(range(0,10,2)))
# print(s1)
# print(s1.iloc[:3]) # 位置[0:3)的元素
# print(s1.iloc[3]) # 位置为3的元素

# # DataFrame
# df1=pd.DataFrame(np.random.randn(6,4),index=list(range(0,12,2)),columns=list(range(0,8,2)))
# print(df1)
# print(df1.iloc[:3]) # 1、2行
# print(df1.iloc[1:5,2:4]) # 
# print(df1.iloc[[1,3,5],[1,3]]) # 2,4,6行，2,4列
# print(df1.iloc[1:3,:]) # 2,3行，所有列
# print(df1.iloc[1]) # 1行

# -----------------Selection by callable----------------------------

# # DataFrame
# df1=pd.DataFrame(np.random.randn(6,4),index=list('abcdef'),columns=list('ABCD'))
# print(df1)
# print(df1.loc[lambda df:df['A']>0,:])
# print(df1.loc[:,lambda df:['A','B']])
# print(df1.iloc[:,lambda df: [0,1]])
# print(df1[lambda df: df.columns[0]])

# # Series
# print(df1['A'].loc[lambda s: s>0])


# # --------------------- Indexing with list with missing labels is deprecated -------------------
# s = pd.Series([1, 2, 3])
# s.loc[[1, 2, 3]]

