'''
list类相关方法使用示例
'''

# -----------------添加---------------
# fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 1]  # 苹果，香蕉，梨，橘子，椰子

# # s.append(x)
# fruit.append('Pitaya')  # 末尾添加火龙果
# fruit.append(['apple', 'banana'])
# fruit[len(fruit):len(fruit)]=['Pitaya']

# # s.insert(index,x)
# fruit.insert(1, 'peach')  # index=1,添加桃子
# fruit[1:1]=['1']

# s.extent(t)
# fruit.extend(['apple', 'banana'])  # 区别于：fruit.append(['apple', 'banana'])
# fruit[len(fruit):len(fruit)]=['apple', 'banana']
# fruit+=['apple', 'banana']

# print('-------------')


# --------------------删除----------------------
# fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 1,'apple']  # 苹果，香蕉，梨，橘子，椰子

# # s.pop([index])
# fruit.pop(1)  # 删除index=1的元素
# fruit.pop()  # 删除最后一个元素：火龙果

# # s.remove(x)
# fruit.remove('apple')  # 移除第一个匹配的苹果

# # s.clear()
# fruit.clear()  # 全部清除

# # del语句
# del fruit[0]
# del fruit[:3]
# del fruit[::2]

# # 索引切片赋值
# fruit[0]=[]
# fruit[:3]=[]
# fruit[::2]=[]
# print('-------------')

# ---------------------修改-------------------
# fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 1,'apple']  # 苹果，香蕉，梨，橘子，椰子
# fruit[0]=0
# fruit[1:4]=[1,2,3]
# fruit[::2]=[0,0,0,0]
# print('-------------')



# --------------查看：长度、最大值、最小值------------
fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut','apple']  # 苹果，香蕉，梨，橘子，椰子
max = max(fruit)  # 'pear'
min = min(fruit)  # 'Coconut'
length = len(fruit)  # 6
fruit[1]  # 'banana'
fruit[::2]  # ['apple',  'pear', 'Coconut']
count=fruit.count('apple')
index=fruit.index('apple') # 0
index1=fruit.index('apple',1) # 5
index2=fruit.index('apple',1,3) # 报错
print('-------------')
