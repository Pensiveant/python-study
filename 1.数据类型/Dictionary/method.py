'''
字典方法使用示例
'''


D={'spam':2,'ham':1,'eggs':3}


# values()、items()
values=list(D.values())
items=list(D.items())
print(values)
print(items)

# get()
value=D.get('test')
print(value)
value1=D.get('test',404)
print(value1)
# print(D['test']) # 报错

# update()
D2={'toast':4,'muffin':5,'eggs':8}
D.update(D2)
print(D)

# pop(key)
eggValue=D.pop('eggs')
# D.pop('test') # 删除不存的key，出错
print(eggValue)
print(D)