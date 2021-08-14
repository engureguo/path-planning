import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator as ML
import DataProcess as R

# type - 坐标类型
# 1     start-point      起点
# 2     table            仪表点
# 3     road-point       道路上的点
# 4     suggested-point  建议观测点

d = R
edges = d.load_edges()
points = d.load_points()

plt.figure(figsize=(10, 15))  # 2:3
plt.xlim(2000, 2400)  # x轴的刻度范围, 400
plt.ylim(1400, 2000)  # y轴的刻度范围, 600
plt.tight_layout()
plt.grid(linestyle='-.')

x_major = ML(10)
y_major = ML(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major)
ax.yaxis.set_major_locator(y_major)


for p in points:
    if p['type'] == 2:  # 仪表点
        plt.plot(p['x'], p['y'], 'o', color='#ED9121')
    else:  # 路径点
        plt.plot(p['x'], p['y'], 'o', color='#0085c3')
        plt.text(p['x'], p['y'], p['no'])

for e in edges:
    # print(str(e['p']) + '\t' + str(e['q'])
    x1, y1 = points[e['p']]['x'], points[e['p']]['y']
    x2, y2 = points[e['q']]['x'], points[e['q']]['y']
    plt.plot((x1, x2), (y1, y2))

plt.show()
# plt.savefig('fig.png')
