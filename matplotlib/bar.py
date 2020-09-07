# 柱状图的绘制
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 创建图表
fig, ax = plt.subplots()

# 标题
ax.set_title('Scores by group and gender')



# 坐标轴
ax.set_ylabel('Scores')

labels = ['G1', 'G2', 'G3', 'G4', 'G5'] # 坐标轴数据
x = np.arange(len(labels))  # the label locations
ax.set_xticks(x)
ax.set_xticklabels(labels)

# 数据
men_means = [20, 34, 30, 35, 27]    
women_means = [25, 32, 34, 20, 25]

width = 0.35  # bar的宽度
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# 图例
ax.legend()

# 在bar上面显示文本，值为其高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()