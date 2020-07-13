'''
创建pandas.DataFrame对象
'''

import pandas as pd
import numpy as np

# # 字典：key为字符串，代表列名；值为Series或列表或同长度的一维ndarray对象或字典，代表一列
# seriesDict={
#     'one':pd.Series([1.,2.,3.],index=['a','b','c']),
#     'two':pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])
# }
# df=pd.DataFrame(seriesDict)
# print(df)

# listDict={
#     'one':[1.,2.,3.,4.], # 默认索引为0,1,2,3...
#     'two':[4.,3.,2.,1.]
# }
# df1=pd.DataFrame(listDict,index=['a','b','c','d'])
# print(df1)

# tupleDict={
#     'one':(1.,2.,3.,4.), # 默认索引为0,1,2,3...
#     'two':(4.,3.,2.,1.)
# }
# df10=pd.DataFrame(tupleDict,index=['a','b','c','d'])
# print(df10)

# ndarrayDic={
#     'one':np.array([1,2,3,4]), # 默认索引为0,1,2,3...
#     'two':np.array([7,8,9,10]),
# }
# df2=pd.DataFrame(ndarrayDic)
# print(df2)

# dictDict={
#     'one':{'a':1.,'b':2,'c':3.},    
#     'two':{'a':1.,'b':2,'c':3.,'d':4.}
#     }
# df3=pd.DataFrame(dictDict)
# print(df3)


# # 列表：每个元素为Series或列表或同长度的一维ndarray对象或字典，代表一行

# seriesList=[pd.Series([1.,2.,3.],index=['a','b','c']),pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])]
# df4=pd.DataFrame(seriesList,index=['one','two'])
# print(df4)

# listList=[[1.,2.,3.,4.], # 默认索引为0,1,2,3...
#           [4.,3.,2.,1.]]
# df5=pd.DataFrame(listList,index=['one','two'],columns=['a','b','c','d'])
# print(df5)

# ndarrayList=[np.array([1,2,3,4]), # 默认索引为0,1,2,3...
#              np.array([7,8,9,10])]
# df6=pd.DataFrame(ndarrayList,index=['one','two'])
# print(df6)

# dictList=[{'a':1.,'b':2,'c':3.},{'a':1.,'b':2,'c':3.,'d':4.}]
# df7=pd.DataFrame(dictList,index=['one','two'])
# print(df7)

# # 2维numpy.ndrray对象
# twoDNdarray=np.array([[1,2,3],[4,5,6]])
# df8=pd.DataFrame(twoDNdarray,index=['one','two'],columns=['a','b','c'])
# print(df8)

# # DataFrame
# dataFrame=pd.DataFrame(data=[[1,2,3],[4,5,6],[4,5,6]],index=['one','two','tree'],columns=['a','b','c'])
# print(dataFrame)
# df9=pd.DataFrame(dataFrame,copy=True)
# print(df9)

# 字典，成员为元组
dictOfTuple={
        ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
        ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
        ('a', 'c'): {('A', 'B'): 5,('A', 'C'): 6},
        ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
        ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
        }
df7=pd.DataFrame(dictOfTuple)
print(df7)