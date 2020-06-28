import struct
import os

filepath=r'D:\pensiveant\github\python-study\radar\Z_RADR_I_Z9230_20200601190100_O_DOR_SA_CAP.bin'
binFile=open(filepath,'rb')
size=os.path.getsize(filepath)
for i in range(size):
    data=binFile.read(1) # 读取一个字节
    print(data)
binFile.close()