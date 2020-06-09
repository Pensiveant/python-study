x=77
def func():
    global x
    x=99
func()
print(x)

# 在函数中定义全局变量y
x=77
def func():
    global y
    y=99
func()
print(y) # 输出99