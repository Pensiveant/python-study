'''
遍历文件夹
'''
import os

for root,dirs,files in os.walk(r'D:\pensiveant\lab\python\user',topdown=False):
    print(root)
    print(dirs)
    print(files)