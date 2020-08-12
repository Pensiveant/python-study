'''
list类相关方法使用示例
'''

# 添加
# s.extent(t)
# s.insert(i,x)
# s.append(x)
fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 1]  # 苹果，香蕉，梨，橘子，椰子
fruit.extend(['apple', 'banana'])  # 序列添加：苹果，香蕉
fruit.insert(1, 'peach')  # index=1,添加桃子
fruit.append('Pitaya')  # 末尾添加火龙果


# 删除
fruit = ['apple', 'banana', 'pear', 'orange', 'Coconut', 1]  # 苹果，香蕉，梨，橘子，椰子
fruit.pop(1)  # 删除第二个元素
fruit.pop()  # 删除最后一个元素：火龙果
fruit.remove('apple')  # 移除苹果
fruit.clear()  # 全部清除


# 查看：长度、最大值、最小值
