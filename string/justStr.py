centerStr='pensiveant'
print(centerStr.center(20,'0')) # 00000pensiveant00000
print(centerStr) # pensiveant

leftStr='pensiveant'
print(leftStr.ljust(20,'0')) # pensiveant0000000000
print(leftStr) # pensiveant

rightStr='pensiveant'
print(rightStr.rjust(20,'0')) # 0000000000pensiveant
print(rightStr) # pensiveant

# 
zfillStr='pensiveant'
print(zfillStr.zfill(20)) # 0000000000pensiveant
print(zfillStr) # pensiveant