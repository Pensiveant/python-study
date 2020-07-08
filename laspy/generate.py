'''
生成.las文件
'''

import laspy

lazFile=laspy.file.File(r'D:\pensiveant\github\python-study\laspy\20120414_002130.laz', mode="r")

hdr = laspy.header.Header(file_version=1.4, point_format=7)
path=r'D:\pensiveant\github\python-study\laspy\radar.las'
outFile= laspy.file.File(path, mode='w', header=hdr)
outFile.x=lazFile.x[:10]
outFile.y=lazFile.y[:10]
outFile.z=lazFile.z[:10]
outFile.intensity=[1,2,3,4,5,6,7,8,9,10]
outFile.close()