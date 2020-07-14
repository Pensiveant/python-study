'''
DataFrame使用示例
'''

import pandas as pd

# --------------索引-------------------
dataFrame=pd.DataFrame([[70,80,90],[99,56,89],[67,10,79],[97,80,79]],index=['张三','李四','王五','赵六'],columns=['高数','马克思主义','线性代数'])
print(dataFrame)


# 一项
item=dataFrame['张三','高数']
print(item)

# 选择一行或多行
aRow=dataFrame.loc['张三'] # 选择'张三'行
twoRow=dataFrame.iloc[2] # 选择第二行
twoToThreeRow=dataFrame[1:3] # 选择2-3行

# 选择一列或多列
oneCol=dataFrame['高数'] # 选择'高数'列
oneCol=dataFrame.loc[:,'高数']
print(oneCol)

