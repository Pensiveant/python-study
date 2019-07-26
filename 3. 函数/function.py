# coding=UTF-8
# 定义函数语法实践
def sum(x,y):
    return x+y
print(sum(1,3))
# 默认参数函数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*n
    return s



# 定义阶乘函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))
