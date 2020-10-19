import numpy as np


## -----------------------ndarray.item(*args)--------------------------

# array = np.array([1])
# array1=np.array([1,23])
# itemNone=array.item() # 1,只对size=1的有效
# itemNone1=array1.item() # 报错：can only convert an array of size 1 to a Python scalar

# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# itemNumber=array.item(8) # 9，按行索引，相当于第9个元素
# itemNumber1 = array.item((2, 1)) # 8,等价于第3行，第2个元素

# print('ndarray.item(*args)')

## -----------------------------ndarray.tolist()-------------------------

# 1. 对应一维数组，`tolist()`方法和`list()`方法基本相同。不同点在于tolist()方法，将numpy的数据类型转换为了python的数据类型即示例中的`'numpy.int32'->'int'`
# array=np.array([1,2,3])
# list1=list(array) # [1,2,3]
# type1=type(list1[0]) # <class 'numpy.int32'>
# list2=array.tolist() # [1,2,3]
# type2=type(list2[0]) # <class 'int'>

# 2. 对于二维数组，`tolist()`递归应用于每个元素
# array=np.array([[1,2,3],[4,5,6]])
# list1=list(array) # [array([1, 2, 3]), array([4, 5, 6])]
# list2=array.tolist() # [[1, 2, 3], [4, 5, 6]]

# 3. 对于0维数组，`tolist()`有效，`list()`将报错
# array = np.array(1)
# list1=list(array)
# list2=array.tolist() # 1

# print('ndarray.tolist()')

## ----------------------------------------------------------------ndarray.itemset(*args)----------------------------------

# 1. 基本用法，修改对应位置值
# array=np.array([1]) # [1]
# itemSet1=array.itemset(3) # None
# list1=array.tolist() # [3]

# array1=np.array([[1,2,3],[4, 5, 6]]) #  [[1, 2, 3], [4, 5, 6]]
# itemSet2=array1.itemset((1,1),9999)
# list2=array1.tolist() # [[1, 2, 3], [4, 9999, 6]]

# # 2. 传入的参数只有一个时，只对size=1的数组有效，其他的报错
# array=np.array([1,2,3])
# itemSet1=array.itemset(3) # 

# print('ndarray.itemset()')

## ---------------------------ndarray.tobytes() ------------------------




