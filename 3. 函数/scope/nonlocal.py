'''
通过nonlocal表达式，可以修改外层函数的变量
'''

# def normalfunc():
#     x = 88
#     def nestedfunc():
#         x = 77
#     nestedfunc()
#     print(x)
# normalfunc()

# def nonlocalfunc():
#     y = 88
#     def nestedfunc():
#         nonlocal y
#         y = 77
#     nestedfunc()
#     print(y)
# nonlocalfunc()

# nonlocal表达式，对应的变量必须在外层已经定义

def nonlocalVar():
    x=66
    def nestedfunc():
        nonlocal y
        y = 77
    nestedfunc()
    print(x,y)
nonlocalVar() # 报错，no binding for nonlocal 'y' found
