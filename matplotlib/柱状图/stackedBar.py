# 堆叠柱状图
# 使用bottom关键字参数进行堆叠以及yeer关键字参数设置误差条
# reference:https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体

fig, ax = plt.subplots()

labels=['G1','G2','G3','G4','G5'] # 分组
men_means=[20,34,30,35,27] # 男生得分的平均值
women_means=[25,32,34,20,25] # 女生得分的平均值
men_std=[2,3,4,1,2] # 标准差
women_std=[3,5,2,3,3] # 标准差
width=0.35 # 柱体宽度

ax.bar(labels,men_means,width,yerr=men_std,label='男生')
ax.bar(labels,women_means,width,yerr=women_std,bottom=men_means,label='女生')

ax.set_ylabel('分数')
ax.set_title('不同组和性别的得分情况')
ax.legend()

plt.show()
