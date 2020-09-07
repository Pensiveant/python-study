import matplotlib.pyplot as plt
import numpy as np
import matplotlib


#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


x=np.linspace(0,2,100)
fig,ax=plt.subplots(2,2)
ax[0][0].plot(x,x,label='x') # 绘制x
ax[0][0].plot(x,x**2,label='x的平方') # 绘制x的平方
ax[0][0].plot(x,x**3,label='X的立方') # 绘制x的立方
ax[0][0].set_xlabel('x轴') # 设置X轴标签
ax[0][0].set_ylabel('y轴') # 设置Y轴标签
ax[0][0].legend() # 添加图例

# 柱状图
xData=['周一','周二','周三','周四','周五']
yData=[100,200,10,400,100]
ax[0][1].bar(xData,yData)

# 饼状图
labels= 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes= [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
ax[1][0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax[1][0].axis('equal') 

# 散点图
scatterxData=[10,3,20,4]
scatteryData=[100,20,130,90]
ax[1][1].scatter(scatterxData,scatteryData)
plt.show()