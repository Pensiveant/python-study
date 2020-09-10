# 基本用法
class FirstClass:
    def setData(self, data):
        self.data = data

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setData('King Arthur')
y.setData('3.1415926')

x.display()
y.display()
x.anotehrname = 'spam'


# 继承
class SecondClass(FirstClass):
    def display(self):
        print('Current value="%s"' % self.data)


z = SecondClass()
z.setData('42')
z.display()


# 运算符重载
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass:%s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()  # Current value="abc"
print(a)  # [ThirdClass:abc]
b = a+'xyz'
b.display()  # Current value="abcxyz"
print(b)  # [ThirdClass:abcxyz]
a.mul(3)
print(a)  # [ThirdClass:abcabcabc]
