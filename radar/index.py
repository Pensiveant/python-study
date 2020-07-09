from PyRadar import Radar
from PyRadar import ppi
import laspy 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图
from scipy.interpolate import griddata
import copy

k = Radar(r'D:\pensiveant\github\python-study\radar', '\Z_RADR_I_Z9230_20200601190600_O_DOR_SA_CAP.bin')  




# # 绘制散点图
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(k.x[0:1500], k.y[0:1500], k.z[0:1500])
 
 
# # 添加坐标轴(顺序是Z, Y, X)
# ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
# ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
# ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
# plt.show()

# hdr = laspy.header.Header(file_version=1.4, point_format=7)
# outfile = laspy.file.File(r'D:\pensiveant\github\python-study\radar\radar.las', mode="w", header=hdr)

inFile = laspy.file.File(r'D:\pensiveant\github\python-study\radar\20120414_002130.laz',mode= "r")
new_header = copy.copy(inFile.header)
# new_header.format = 1.4
# new_header.pt_dat_format_id = 7
outfile = laspy.file.File(r'D:\pensiveant\github\python-study\radar\radar.las', mode= "w",vlrs = inFile.header.vlrs, header = new_header)

xmin = np.floor(np.min(k.x))
xmax=np.floor(np.max(k.x))
ymin = np.floor(np.min(k.y))
ymax=np.floor(np.max(k.y))
zmin = np.floor(np.min(k.z))
zmax=np.floor(np.max(k.z))

# 设置公共头部块
# outfile.header.offset = [xmin,ymin,zmin]
# outfile.header.scale = [1.00,1.00,1.00]
outfile.header.max=[xmax,ymax,zmax]
outfile.header.min= [xmin,ymin,zmin]
# outfile.header.vlr=laspy.header.VLR('LASF_Projection','2112',)

outfile.X = k.x
outfile.Y = k.y
outfile.Z = k.z
# outfile.red= [255 for i in range(0, k.x.size)]
# outfile.green= [0 for i in range(0, k.x.size)]
# outfile.blue= [0 for i in range(0, k.x.size)]
outfile.intensity = k.r
outfile.flag_byte = [100 for i in range(0, k.x.size)]
outfile.raw_classification = [11 for i in range(0, k.x.size)]
outfile.user_data = [0 for i in range(0, k.x.size)]
outfile.pt_src_id = [10507 for i in range(0, k.x.size)]
outfile.gps_time = [18478084.36583805 for i in range(0, k.x.size)]
# outfile.classification=[11 for i in range(0, k.x.size)]
# outfile.classification_flags=[11 for i in range(0, k.x.size)]
# outfile.pt_src_id=[i for i in range(0, k.x.size)]
outfile.close()



# k.Name   # 文件名字，形如 Z_RADR_I_Z9250_20160701234600_O_DOR_SA_CAP
# k.RawData  # 原始数据
# k.Count  # 径向数据数量（= .bin文件大小/2432）
# k.RawArray  # 原始矩阵 共Count行
# k.NumberOfElevation  # 仰角数量
# k.StartOfReflectivity  # 反射率数据起点，即第一个反射率数据到雷达距离 
# k.StartOfSpeed  # 速度数据起点，即第一个数据到雷达中心的距离
# k.StepOfReflectivity  # 反射率数据库长
# k.StepOfSpeed  #速度库长
# k.NumberOfReflectivity  # 反射率库数
# k.NumberOfSpeed  # 速度库数
# k.PointerOfReflectivity  # 反射率第一个数据指针，第xxx字节
# k.PointerOfSpeed  #速度第一个数据指针
# k.PointerOfSpectralWidth  # 谱宽第一个数据指针
# k.ResolutionOfSpeed  # 速度分辨率
# k.vcp  # 体扫模式
# k.Elevation  # 仰角
# k.Azimuth  # 方位角
# k.Storage  # 存储所有数据的列表
# k.AllInfo  # [[], [], [], []]  # 仰角 方位角 距离 反射率
# k.x  # 直角坐标系里的横坐标
# k.y  # 纵坐标
# k.z  # 竖坐标
# k.r  # 反射率值
# k.elevation_list  # 该体扫模式下的仰角列表
# k.grid_data  # 返回标准化网格数据数组，并保存为.npz文件，网格为500*500*500,可用于体绘制，任意高度CAPPI绘制和雷达回波外推的神经网络训练，此属性计算时间稍长
# k.draw()  #快速画出0.5度仰角的所有反射率值
# k.ppi(0) # 画出给定仰角的ppi图像，参数浮点型
# k.rhi(0)  # 画出给定方位角rhi图像，参数浮点型
# k.cappi(0)  #画出给定高度cappi图像,参数整型，数值0—19之间
# k.points()  # 三维散点图，开始交互可视化
# k.surface()  # 三维等值面图，开始交互可视化
# k.render()  #体绘制交互


# ppi(r'D:\pensiveant\github\python-study\radar\Z_RADR_I_Z9230_20200601190100_O_DOR_SA_CAP.bin')  # 快速绘制0.5度仰角ppi图像，大概5秒一张

# def grid(self):
#     GRID_RESOLUTION = 500  # 网格分辨率，可修改
        
#     x, y, z, r = self.x, self.y, self.z, self.r
#     grid_x, grid_y, grid_z = np.mgrid[min(x):max(x):GRID_RESOLUTION*1j, min(y):max(y):GRID_RESOLUTION*1j, min(z):max(z):GRID_RESOLUTION*1j]  # 构建三维网格，方形，体绘制适用
        
#     x = x[np.newaxis,:]
#     y = y[np.newaxis,:]
#     z = z[np.newaxis,:]
        
#     points = np.concatenate((x,y,z),axis=0).T
        
#     grid_r = griddata(points, r, (grid_x, grid_y, grid_z), method = 'nearest')  # 返回结果，三维数组

#     hdr = laspy.header.Header(file_version=1.4, point_format=7)
#     outfile = laspy.file.File(r'D:\pensiveant\github\python-study\radar\radar.las', mode="w", header=hdr)
#     xmin = np.floor(np.min(grid_x.ravel()))
#     ymin = np.floor(np.min(grid_y.ravel()))
#     zmin = np.floor(np.min(grid_z.ravel()))
#     outfile.header.offset = [xmin,ymin,zmin]
#     outfile.header.scale = [0.001,0.001,0.001]
#     outfile.x = np.array(grid_x.ravel())
#     outfile.y = np.array(grid_y.ravel())
#     outfile.z = np.array(grid_z.ravel())
#     outfile.Intensity = grid_r.ravel()
#     outfile.close()

# grid(k)