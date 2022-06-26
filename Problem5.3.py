import numpy as np
import cvxpy as cp
import scipy as sp
import control as ctrl
import polytope as pc
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.linalg as spla
from polytope import plot
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from IPython.core.pylabtools import figsize
from matplotlib.patches import Circle
import math

mpl.rcParams['text.usetex'] = True  # 全局开启
mpl.rcParams['font.family'] = 'Times New Roman'  # 指定字体
figsize(9, 6)

x_0 = [np.array([[0.1], [0.1]]), np.array([[0.2], [0.2]]), np.array([[-0.1], [-0.1]]), np.array([[-0.1], [0.1]])]
x_1_list = []
x_2_list = []
for j in range(4):

    x_i_list = [None] * 51
    x_i_list[0] = x_0[j]
    x_1 = [None] * 51
    x_2 = [None] * 51
    x_1[0] = x_0[j][0, 0]
    x_2[0] = x_0[j][1, 0]

    for i in range(50):

        x_1[i+1] = x_1[i] / 5 + math.cos(x_2[i]) - 1
        x_2[i+1] = (math.exp(x_1[i]) * x_2[i]) / 2

    x_1_list.append(x_1)
    x_2_list.append(x_2)

# for i in range(4):
plt.plot(x_1_list[0], x_2_list[0], label = r"$x_0=[0.1 \hspace{0.5em} 0.1]^\mathrm{T}$",ls = '-.')
plt.plot(x_1_list[1], x_2_list[1], label = r"$x_0=[0.2 \hspace{0.5em} 0.2]^\mathrm{T}$",ls = '-.')
plt.plot(x_1_list[2], x_2_list[2], label = r"$x_0=[-0.1 \hspace{0.5em} -0.1]^\mathrm{T}$",ls = '-.')
plt.plot(x_1_list[3], x_2_list[3], label = r"$x_0=[-0.1 \hspace{0.5em} 0.1]^\mathrm{T}$",ls = '-.')
# print(x_1,x_2)
# plt.xlim([-2, 2])
# plt.ylim([-2, 2])
plt.xlabel(r"$a_{t}$", size=35, labelpad=5)
plt.ylabel(r"$b_{t}$", size=35, labelpad=15)
plt.tick_params(labelsize=23)

plt.legend(bbox_to_anchor=(0.3,1),#图例边界框起始位置
                 loc="upper right",#图例的位置
                 ncol=1,#列数
                 mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
                 borderaxespad=0,#坐标轴和图例边界之间的间距
                 title=r"$x_0$ position",#图例标题
                 shadow=False,#是否为线框添加阴影
                 fancybox=True)#线框圆角处理参数

plt.show()
