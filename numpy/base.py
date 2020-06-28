import numpy as np

a=np.arange(15).reshape(3,5)
print(a) #[[ 0  1  2  3  4],[ 5  6  7  8  9],[10 11 12 13 14]]
print(a.ndim) # 2
print(a.shape) # (3,5)
print(a.dtype) # int32
print(a.itemsize) # 4
print(a.data) # <memory at 0x00000204E33F5110>