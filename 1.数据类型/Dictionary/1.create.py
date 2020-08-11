'''
创建字典示例
'''

# 字面量语法

dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 123, 98.6: 37}
dict3 = {('name'): 'pensiveant', ('age'): 18}
print('--------------')

# 构造函数
dict5 = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # 位置参数为可迭代对象
dict6 = dict([('two', 2), ('one', 1), ('three', 3)])  # 位置参数为可迭代对象
dict4 = dict(one=1, two=2, three=3) # 位置参数为空，关键字参数三个
dirct7 = dict({'three': 3, 'one': 1, 'two': 2},three=4,four=4) # 位置参数为可映射对象，关键字参数两个
print('--------------')


# 类方法
dict8=dict.fromkeys(['one','two','three']) # 每个key的值默认为None
dict9=dict.fromkeys(['one','two','three'],1) # 每个key的值为1
dict10=dict.fromkeys(['one','two','three'],[1,2,3]) # 每个key的值都为[1,2,3]，而不是{ 'one': 1, 'two': 2,'three': 3}
print('--------------')
