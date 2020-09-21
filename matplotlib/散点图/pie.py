# 绘制饼图
# reference:https://echarts.apache.org/examples/zh/editor.html?c=pie-custom
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'
fig, ax = plt.subplots()

labels =['直接访问','邮件直销','联盟广告','视频广告','搜索引擎']
datas=[335,310,274,235,400]

ax.pie(datas, labels=labels,startangle=90)

plt.show()

