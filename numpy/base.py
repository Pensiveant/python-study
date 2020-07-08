import numpy as np

# a=np.arange(15).reshape(3,5)
# print(a) #[[ 0  1  2  3  4],[ 5  6  7  8  9],[10 11 12 13 14]]
# print(a.ndim) # 2
# print(a.shape) # (3,5)
# print(a.dtype) # int32
# print(a.itemsize) # 4
# print(a.data) # <memory at 0x00000204E33F5110>

## ------基本操作----
# a=np.array([20,30,40,50]) # [20 30 40 50]
# b=np.arange(4)  # [0 1 2 3]
# c=a+b # [20 31 42 53]
# print(c)
# d=b**2 #  [0 1 4 9]
# print(d)

# A=np.array([[1,1],[0,1]])
# B=np.array([[2,0],[3,4]])
# C=A*B  # [[2 0]
#         # [0 4]]
# print(C)
# C1=A@B # [[5 4]
#         #  [3 4]]
# printa(C1)
# C2=A.dot(B)# [[5 4]
#         #  [3 4]]
# print(C2)

# rg=np.random.default_rng(1)
# a=np.ones((2,3),dtype=int) # [[1 1 1]
#                          #    [1 1 1]]
# b=rg.random((2,3)) 
# print(b)
# a*=3              # [[3 3 3]
#                    # [3 3 3]]
# print(a)
# b+=a
# print(b)

# a = np.ones(3, dtype=np.int32)
# b = np.linspace(0,np.pi,3)
# c = a+b
# print(c.dtype.name) # float64


# a=np.array([1,2,3,4,5])
# print(a.sum())
# print(a.min())
# print(a.max())

# # 通用函数
# B=np.arange(3)
# print(B) # [0 1 2]
# print(np.exp(B)) # 指数运算（e^0,e^1,e^2）:[1.         2.71828183 7.3890561 ]
# print(np.sqrt(B)) # 开方运算
# C=np.array([2,-1,4.])
# print(C) # [ 2. -1.  4.]
# print(np.add(B,C)) # 加法运算:[2. 0. 6.]


## ----索引、切片和迭代----

# a=np.arange(10)**3
# print(a)
# print(a[2])
# print(a[2:5])
# for value in a:
#     print(value)

# def f(x,y):
#     return 10*x+y
# b=np.fromfunction(f,(5,4),dtype=int)
# print(b)
# print(b[2,3])
# print(b[0:5,1])


##  ----形状操作----
# rg=np.random.default_rng(1)
# a=np.floor(10*rg.random((3,4)))
# print(a.shape) # (3, 4)
# ravleShape=a.ravel()
# print(ravleShape.shape) # (12,)
# reshape=a.reshape(6,2)
# print(reshape.shape)# (6,2)
# tShape=a.T
# print(tShape.shape) # (4, 3)

## ---复制-----
# # 未拷贝
# a=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
# b=a
# print(b is a) # true

# # 浅拷贝
# c=a.view()
# print(c)
# print(c is a) # False
# print(c.base is a) # True
# print(c.flags.owndata) # False
# c=c.reshape((2,6))
# print(c)
# print(a.shape) # (3, 4)
# c[0,4]=1234
# print(a) # [[   0    1    2    3]
#          #  [1234    5    6    7]
#         #   [   8    9   10   11]]

# s=a[:,1:3]
# print(s)
# s[:]=10
# print(a) # [[   0   10   10    3]
#          #  [1234   10   10    7]
#         #   [   8   10   10   11]]

# # 深拷贝
# d=a.copy()
# print(d is a) # False
# print(d.base is a) # False
# d[0,0]=999
# print(a) # [[   0   10   10    3]
#          #  [1234   10   10    7]
#         #   [   8   10   10   11]]


## ----高级索引和索引技巧------
# a=np.arange(12)**2
# print(a) # [  0   1   4   9  16  25  36  49  64  81 100 121]
# i=np.array([1,1,3,8,5])
# print(a[i]) # [ 1  1  9 64 25]

# j=np.array([[3,4],[9,7]])
# print(a[j]) # [[ 9 16]
#             #  [81 49]]



# palette=np.array([[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,255]])
# image=np.array([[0,1,2,0],[0,3,4,0]])
# print(palette[image]) # [[[  0   0   0]
#                       #   [255   0   0]
#                       #   [  0 255   0]
#                       #   [  0   0   0]]

#                      #   [[  0   0   0]
#                      #    [  0   0 255]
#                         # [255 255 255]
#                         # [  0   0   0]]]

a=np.arange(12).reshape(3,4)
print(a) # [[ 0  1  2  3]
        #   [ 4  5  6  7]
        #   [ 8  9 10 11]]
i=np.array([[0,1],[1,2]])
j=np.array([[2,1],[3,3]])
print(a[i,j]) # [[ 2  5]
            #    [ 7 11]]
