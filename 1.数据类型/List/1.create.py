'''
创建列表
'''

# 字面量语法
fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 5]  # 苹果，香蕉，梨，橘子，椰子

# list 理解
list1 = [(str(item)+'100') for item in fruit] # ['apple100', 'banana100', 'pear100', 'orange100', 'Coconut100', '5100']


# 构造函数
list2 = list('abcd')  # ['a','b','c','d']
list3 = list((1, 2, 3))  # [1,2,3]

print('----------------')
