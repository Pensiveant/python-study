# list 学习示例

# 定义list
print('定义list------')
fruit=['apple','banana','pear','orange','Coconut',1] # 苹果，香蕉，梨，橘子，椰子
print(fruit)

# print(max(fruit))



## 添加
print('添加数据')
addFruit=[]
# 序列添加
addFruit.extend(['apple','banana','pear','orange','Coconut']) # 苹果，香蕉，梨，橘子，椰子
# index=1,添加桃子
addFruit.insert(1,'peach')
# 末尾添加火龙果
addFruit.append('Pitaya')
print(addFruit)


## 删除
print('删除数据')
deleteFruit=['apple','banana','pear','orange','Coconut','peach','Pitaya'] # 苹果，香蕉，梨，橘子，椰子，桃子，火龙果
del deleteFruit[-1] # 删除最后一个元素：火龙果
deleteFruit.pop(1) # 删除第二个元素
deleteFruit.pop() # 删除最后一个元素：火龙果
deleteFruit.remove('apple') # 移除苹果
deleteFruit.clear() # 全部清除
print(deleteFruit)

## 修改

modifyFruit=['apple','banana','pear','orange','Coconut','peach','Pitaya'] # 苹果，香蕉，梨，橘子，椰子，桃子，火龙果
modifyFruit[1]=1 # 第二个元素修改为1
print(modifyFruit)