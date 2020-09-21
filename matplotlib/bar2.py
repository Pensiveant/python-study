# reference:https://echarts.apache.org/examples/zh/editor.html?c=bar-background

import matplotlib
import matplotlib.pyplot as plt


figure,ax= plt.subplots()

xlabel=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data=[120, 200, 150, 80, 70, 110, 130]
ax.bar(xlabel,data,bottom=100,color='#c23531')

plt.show()
