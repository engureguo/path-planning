import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator as ML

# 栅格demo

plt.figure(figsize=(10, 15))
plt.xlim(2000, 2400)  # x轴的刻度范围
plt.ylim(1400, 2000)  # y轴的刻度范围
plt.tight_layout()
plt.grid(linestyle='-.')

x_major = ML(10)
y_major = ML(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major)
ax.yaxis.set_major_locator(y_major)

plt.show()

# 设置刻度 https://www.jb51.net/article/163842.htm
