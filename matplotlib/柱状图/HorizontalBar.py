# 水平柱状图
# 使用 Axes.barh()绘制水平柱状图
# reference:https://matplotlib.org/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()


np.random.seed(19680801)
people=('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos=np.arange(len(people))
performance=3+10*np.random.rand(len(people))
error=np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()