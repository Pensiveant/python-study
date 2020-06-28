import pandas as pd
import numpy as np

# -------------------Series------------------------

# # from ndarray
# s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s)
# print(s.index)

# s1=pd.Series(np.random.randn(5))
# print(s1)

# # from dict
# d={'b':1,'a':0,'c':2}
# s2=pd.Series(d)
# print(s2)
# s3=pd.Series(d,index=['b','c','d','a']) # 给定索引后，将从字典对应key中取值，没有则为NaN
# print(s3)

# # from scalar value
# s4=pd.Series(5,index=['a','b','c','d','e'])
# print(s4)

# # Series is ndarray-like
# print(s[0])
# print(s[:3])
# print(s[s>s.median()])
# print(s[[4,3,1]])
# print(np.exp(s))

# print(s.dtype)
# print(s.array)
# print(s.to_numpy())

# # Series is dict-like

# s5=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s5)
# s5['a']=2
# print(s5)
# print(s5['a'])
# print(s5.get('a'))

# # Vectorized operations and label alignment with Series

# s6=pd.Series(7,index=['a','b','c','d','e'])
# print(s6+s6)
# print(s6*4)
# print(np.exp(s6))

# # Name attribute

# nameS=pd.Series(np.random.randn(5),name='something')
# print(nameS)
# changeNameS=nameS.rename('different')
# print(changeNameS)


# --------------------DataFrame-------------------------

# 字典，成员为panda的Series对象（一列）
# d={
#     'one':pd.Series([1.,2.,3.],index=['a','b','c']),
#     'two':pd.Series([1.,2.,3.,4.],index=['a','b','c','d'])
# }
# df=pd.DataFrame(d)
# print(df)

# # 字典，成员为字典(一列)
# dictDict={
#     'one':{'a':1.,'b':2,'c':3.},
#     'two':{'a':1.,'b':2,'c':3.,'d':4.}
#     }
# df5=pd.DataFrame(dictDict)
# print(df5)

# df2=pd.DataFrame(d,index=['d','b','a'])
# print(df2)

# df3= pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
# print(df3)

# # 字典，成员为列表或ndarray对象（一列）
# listDict={
#     'one':[1.,2.,3.,4.],
#     'two':[4.,3.,2.,1.]
# }
# df4=pd.DataFrame(listDict)
# print(df4)

# # 结构化数组或记录数组,示例为定义每列的数据类型，以及每行的数据
# structuredArray=np.zeros((2,),dtype=[('A','i4'),('B','f4'),('C','a10')])
# structuredArray[:]=[
#     (1,2.,'Hello'),
#     (2,3,'world')
# ]
# df5=pd.DataFrame(structuredArray)
# print(df5)

# # 列表，成员为字典（一行）
# listOfDict=[
#     {'a': 1, 'b': 2},
#     {'a': 5, 'b': 10, 'c': 20}
# ]
# df6=pd.DataFrame(listOfDict)
# print(df6)

# # 字典，成员为元组
# dictOfTuple={
#         ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
#         ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
#         ('a', 'c'): {('A', 'B'): 5,('A', 'C'): 6},
#         ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
#         ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
#         }
# df7=pd.DataFrame(dictOfTuple)
# print(df7)

# # 构造函数 DataFrame.from_dict()

# fromDict=dict([('A',[1,2,3]),('B',[4,5,6])])
# df8=pd.DataFrame.from_dict(fromDict)
# print(df8)

# df9=pd.DataFrame.from_dict(dict([('A',[1,2,3]),('B',[4,5,6])]),orient='index',columns=['one','two','three'])
# print(df9)

# # 构造函数DataFrame.from_records(

# fromRecord=[(1, 2., b'Hello'), (2, 3., b'World')]
# df10=pd.DataFrame.from_records(fromRecord)
# print(df10)

# ------Column selection, addition, deletion----
# dataFrame=pd.DataFrame({
#         'one':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'two':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'three':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'flag':{'a':False,'b':False,'c':True,'d':False}
#         })
# print(dataFrame)
# print(dataFrame['one']) # 输出one列
# dataFrame['three']=dataFrame['one']*dataFrame['two'] # three列=one列*two列
# print(dataFrame)

# # 删除
# del dataFrame['two']
# print(dataFrame)
# three = dataFrame.pop('three')
# print(dataFrame)

# # 插入
# dataFrame['foo']='bar'
# print(dataFrame)

# dataFrame['one_trunc'] = dataFrame['one'][:2]
# print(dataFrame)

# dataFrame.insert(1, 'bar', dataFrame['one'])
# print(dataFrame)

# ----Indexing / selection------

# dataFrame=pd.DataFrame({
#         'one':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'two':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'three':{'a':1.,'b':2.,'c':3.,'d':4.},
#         'flag':{'a':False,'b':False,'c':True,'d':False}
#         })
# print(dataFrame)
# print(dataFrame['one']) # 选择one列
# print(dataFrame.loc['a']) # 选择a行
# print(dataFrame.iloc[2]) # 选择第二行
# print(dataFrame[1:3]) # 选择2-3行

# -----Transposing（转置）------
dataFrame=pd.DataFrame({
        'one':{'a':1.,'b':2.,'c':3.,'d':4.},
        'two':{'a':1.,'b':2.,'c':3.,'d':4.},
        'three':{'a':1.,'b':2.,'c':3.,'d':4.},
        'flag':{'a':False,'b':False,'c':True,'d':False}
        })
print(dataFrame)
print(dataFrame.T)


# ---------
df = pd.DataFrame({'foo1': np.random.randn(5),'foo2': np.random.randn(5)})
print(df['foo1'])

