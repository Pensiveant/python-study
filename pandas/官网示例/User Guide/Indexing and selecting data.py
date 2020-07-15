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

 
# -------------- Selecting random samples -------------------

# # Series
# s=pd.Series([0,1,2,3,4,5])
# print(s.sample()) # 无参数将返回一行
# print(s.sample(n=3)) # 返回三行
# print(s.sample(frac=0.5)) # 分数行1/2

# print(s.sample(n=6,replace=False)) # repalce可以重复采样，默认每行只能输出一次
# print(s.sample(n=6,replace=True))

# example_weights = [0, 0, 0.2, 0.2, 0.2, 0.4] # 可以设置每行被抽取的权重
# print(s.sample(n=3,weights=example_weights))

# example_weights2 = [0.5, 0, 0, 0, 0, 0] # 如果权重不等于1，将通过将所有权重除以权重之和来重新归一化。
# print( s.sample(n=1, weights=example_weights2))

# # Dataframe
# df2=pd.DataFrame({'col1':[9,8,7,6],'weight_column':[0.5,0.4,0.1,0]}) # 可以将dataframe中的一列作为权重，传值只需传入列标签
# print(df2.sample(n=3,weights='weight_column'))

# df3=pd.DataFrame({'col1':[1,2,3],'col2':[2,3,4]}) # 可以通过设置axis参数，来随机选择列
# print(df3.sample(n=1,axis=1))

# df4=pd.DataFrame({'col1':[1,2,3],'col2':[2,3,4]}) # 可以使用random_state参数为样本的随机数生成器设置种子,接受参数为整数或NumPy RandomState对象。
# print(df4.sample(n=2,random_state=2))

# ------------------ Setting with enlargement -------------------------------

# # Series
# se=pd.Series([1,2,3])
# print(se)
# se[5]=5
# print(se)

# # DataFrame
# dfi=pd.DataFrame(np.arange(6).reshape(3,2),columns=['A','B'])
# print(dfi)
# dfi.loc[:,'C']=dfi.loc[:,'A']
# print(dfi)

# dfi.loc[3]=5 # 类似于append
# print(dfi)

#  ----------------- Fast scalar value getting and setting ----------------------

# # Series
# s=pd.Series([0,1,2,3,4,5])
# print(s.iat[5])

# # DataFrame
# dates=pd.date_range('1/1/2000',periods=8)
# df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
# print(df.at[dates[5],'A'])
# print(df.iat[3,0])

# df.at[dates[5],'E']=7 # 可以扩充和修改
# df.iat[3,0]=7
# print(df)

# ------------------ Boolean indexing -------------------------

# # Series
# s=pd.Series(range(-3,4))
# print(s)
# print(s[s>0]) # 大于0
# print(s[(s<-1)|(s>0.5)]) # 小于-1或大于0.5
# print(s[~(s<0)]) # 大于0

# # DataFrame
# dates=pd.date_range('1/1/2000',periods=8)
# df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
# print(df[df['A']>0]) # A列大于0的行

# df2=pd.DataFrame({
#     'a':['one','one','two','three','two','one','six'],
#     'b':['x','y','y','x','y','x','x'],
#     'c':np.random.randn(7)
# }) 
# criterion=df2['a'].map(lambda x: x.startswith('t'))  # 可以通过map方法生成更加复杂的条件
# print(df2[criterion])
# print(df2[[x.startswith('t') for x in df2['a']]])
# print(df2[criterion&(df2['b']=='x')])

# -------------------- Indexing with isin ---------------------------------------

# # Series
# s=pd.Series(np.arange(5),index=np.arange(5)[::-1],dtype='int64')
# print(s)
# print(s.isin([2,4,6]))
# print(s[s.isin([2,4,6])])

# print(s[s.index.isin([2,4,6])]) # 相同的方法也可以使用在index对象上
# print(s.reindex([2,4,6]))

# s_mi=pd.Series(np.arange(6),index=pd.MultiIndex.from_product([[0,1],['a','b','c']]))
# print(s_mi)
# print(s_mi.iloc[s_mi.index.isin([(1,'a'),(2,'b'),(0,'c')])])
# print(s_mi.iloc[s_mi.index.isin(['a','c','e'],level=1)])

# # DataFrame
# df=pd.DataFrame({
#     'vals':[1,2,3,4],
#     'ids':['a','b','f','n'],
#     'ids2':['a','n','c','n']
# })

# values=['a','b',1,3]
# print(df.isin(values))

# values1={
#     'ids':['a','b'],
#     'vals':[1,3]
# }
# print(df.isin(values1))

# values3={
#     'ids':['a','b'],
#     'ids2':['a','c'],
#     'vals':[1,3]
# }
# row_mask=df.isin(values3).all(1)
# print(df[row_mask])


# --------------- The where() Method and Masking -------------------------------
# s=pd.Series(np.arange(5),index=np.arange(5)[::-1],dtype='int64')
# print(s[s>0]) # 只返回选中的行
# print(s.where(s>0)) # 返回相同形状的Series

# where接收other参数，用于替换条件未False的值
dates=pd.date_range('1/1/2000',periods=8)
df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
# print(df[df<0])
# print(df.where(df<0,-df))

# # 可以对满足条件的项，进行赋值
# s2=s.copy()
# s2[s2<0]=0
# print(s2)
# df2=df.copy()
# df2[df2<0]=0
# print(df2)

# # 默认情况下，where返回修改后的数据副本。inplace可选参数，可以在不创建副本的情况下修改原始数据：
# df_orig=df.copy()
# print(df_orig)
# df_orig.where(df>0,-df,inplace=True)
# print(df_orig)

# df2=df.copy()
# df2[df2[1:4]>0]=3
# print(df2)

df2=df.copy()
df2.where(df2>0,df2['A'],axis='index')
print(df2)