import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

fig, bar = plt.subplots()
bar.set_title('电影票房')

move_name = ['雷神3:诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记',
             '全球风暴', '降魔传']
bar.set_xticklabels(move_name)


x = range(len(move_name))   
y = [73853, 57767, 22354, 15969, 14839, 8725]
rects = bar.bar(x, y, width=0.5,label='票房')
bar.legend()

# 在bar上面显示文本，值为其高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        bar.annotate(
            '{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center',
            va='bottom'
        )


autolabel(rects)


plt.show()
