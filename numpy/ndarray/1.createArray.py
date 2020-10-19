'''
# 创建ndarray对象
# reference:https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation
'''
import numpy as np

#---------------------- from existing data ------------------------------------------------

### np.array()

# list创建Numpy array
listToArray=np.array([1,3,4,5])
print(listToArray)
print(listToArray.dtype)
listToArray1=np.array([1.1,2.3,4.3])
print(listToArray1)
print(listToArray1.dtype)


# # tuple创建Numpy array
# tupleToArray=np.array([(1,3),(4,5)])
# print(tupleToArray)

# # 创建时指定数据类型
# specifiedType=np.array( [ [1,2], [3,4] ], dtype=complex )
# print(specifiedType)

# ------------------------------Ones and Zeros------------------------------

# 元素未知但大小已知
zerosArray=np.zeros((2,3))
print(zerosArray)
onesArray=np.ones((2,3,4))
print(onesArray)
emptyArray=np.empty((2,3))
print(emptyArray)