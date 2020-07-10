import numpy as np

# baseArray=np.array([[1,2,3,4],[5,6,7,8]])
# item=baseArray.item(5)
# print(item)

# listArray=baseArray.tolist()
# print(listArray)


# # empty(shape, dtype=float, order='C')
# emptyArray=np.empty([2,3]) # 2行3列
# emptyArray1=np.empty((2,3),dtype='int')
# emptyArray2=np.empty((2,3),dtype='int',order='F')
# print(emptyArray1)
# print(emptyArray2)

# # empty_like(prototype, dtype=None, order='K', subok=True, shape=None)
# a=[[1,2,3],[4,5,6]]
# emptLikeArr=np.empty_like(a)
# emptLikeArr1=np.empty_like(a,dtype=float) # 覆盖给定数组的类型int为float
# emptLikeArr2=np.empty_like(a,shape=(1,3)) # 覆盖给定数组的形状(2,3)为(1,3)

# # numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')[source]
# eyeArr=np.eye(3) # (3,3)
# eyeArr1=np.eye(3,4) # (3,4)
# eyeArr2=np.eye(3,k=1) # 对角线索引为1
# eyeArr3=np.eye(3,k=-1) # 对角线索引为-1
# print(eyeArr2)

# # numpy.identity(n, dtype=None)[source]
# identityArr=np.identity(3,dtype=complex)
# print(identityArr)

# numpy.ones(shape, dtype=None, order='C')
onesArr=np.ones((2,3,4))
onesArr1=np.ones((3,4),dtype=complex)
print(onesArr1)
