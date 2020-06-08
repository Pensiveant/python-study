# # 普通情况
# def f(a, b, c):
#     print(a, b, c)

# f(1, 2, 3)
# f(c=3, b=2, a=1)
# f(1, c=3, b=2)

# # 默认参数
# def f(a, b=2, c=3):
#     print(a, b, c)

# f(1)
# f(a=1)

# f(1,4)
# f(1,4,5)

# f(1,c=6)


# 任意参数

# def f(*args):
#     print(args)
# f()
# f(1)
# f(1,2,3,4)

# def f(**args):
#     print(args)
# f()
# f(a=1,b=2)


def f(a,*pargs,**kargs):
    print(a,pargs,kargs)
f(1,2,3,x=1,y=2)
