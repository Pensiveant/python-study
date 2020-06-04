'''
获取文件或文件夹的信息
'''

import os

fd=os.open(r'D:\pensiveant\lab\python\condition.py',os.O_APPEND)

# fo=os.fdopen(fd)
stat=os.fstat(fd)
createTime=stat.st_ctime
modifyTime=stat.st_mtime
accessTime=stat.st_atime
