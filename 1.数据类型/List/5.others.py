
import copy

# --------拷贝--------------
ball=['badminton','Table Tennis','Football','Basketball',{'name':'golf'}]

# # 浅拷贝
# ball1=ball.copy()
# ball2=ball[:]
# ball[-1]['name']='others' # 导致ball1、ball2也被修改

# # 深拷贝
# ball1=copy.deepcopy(ball) 
# ball[-1]['name']='others'  # 并不会导致ball1被修改
# print('------------------------')

# ---------------翻转-------------
# numbers=[1,2,3,4,5,6]
# numbers1=numbers.reverse() # [6,5,4,3,2,1]
# print('------------------------')

# -----------------排序--------------

ball=['badminton','Table Tennis','Football','Basketball']
ball.sort() # ball:['Basketball','Football','Table Tennis','badminton']
print('------------------------')
