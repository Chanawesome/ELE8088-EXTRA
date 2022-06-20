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



mpl.rcParams['text.usetex'] = True  # 全局开启
mpl.rcParams['font.family'] = 'Times New Roman'  # 指定字体
figsize(9, 6)

A = np.array([[0.5,0.8],[-1.5,0.2]])
x_0 = np.array([[0.5], [0.5]])
x_i_list = [None] * 51
x_i_list[0] = x_0
x_1_list = [x_0[0, 0]]
x_2_list = [x_0[1, 0]]
y_i_list = [0]
for i in range(50):
    x_i_list[i+1] = A @ x_i_list[i]
    x_1_list.append(x_i_list[i + 1][0, 0])
    x_2_list.append(x_i_list[i + 1][1, 0])
# print(x_1_list)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x_1_list, x_2_list,'-*')
cir1 = Circle(xy=(0.0, 0.0), radius=1, alpha=0.5, color='pink')
ax.add_patch(cir1)

x, y = 0, 0
ax.plot(x, y, 'ro')

plt.axis('scaled')
plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length

plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel(r"$x_{1}$", size=35, labelpad=5)
plt.ylabel(r"$x_{2}$", size=35, labelpad=15)
plt.tick_params(labelsize=23)
grid_xy = [-2, -1, 0, 1, 2]
for i in range(5):
    plt.plot(np.linspace(-2.2, 2.2, 1000), np.linspace(grid_xy[i], grid_xy[i], 1000), lw=2, color="#969696",
             alpha=0.5, zorder=-1)
    plt.plot(np.linspace(grid_xy[i], grid_xy[i], 1000), np.linspace(-2.2, 2.2, 1000), lw=2, color="#969696",
             alpha=0.5, zorder=-1)
# 隐藏上边和右边的框
plt.show()
