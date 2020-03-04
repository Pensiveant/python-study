import numpy as np
import pandas as pd

# 本示例为如何生成pandas支持的数据结构Series以及DataFrame
# @author:pensiveant
# @reference:https://www.pypandas.cn/docs/getting_started/10min.html#%E7%94%9F%E6%88%90%E5%AF%B9%E8%B1%A1

# 通过列表生成Series
s=pd.Series([1,3,5,np.nan,6,8])


# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame
dates=pd.date_range('20200304',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))


# 用Series字典对象生成DataFrame
df2=pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20200304'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(['test','train','test','train']),
    'F':'foo'
})
print(df2.any)


