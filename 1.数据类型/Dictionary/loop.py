D={'name':'pensiveant','job':'码农','age':'保密'}

for key in D: # 等价于 for key in D.keys()
    print(key,D[key])

for key,value in D.items():
    print(key,value)
