import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


data = pd.read_excel("2.1.xlsx")
data = np.array(data)

mean_air_temperature = data[:,0]
height = data[:,1]


# 2.1.a
# 规定横坐标的长度
x1 = np.linspace(31, 37, 28)
# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model0 = make_interp_spline(mean_air_temperature, height)
ys0 = model0(x1)
plt.figure()
# 开始绘图
plt.subplot(2,2,1)
# 绘制散点图
plt.scatter(mean_air_temperature, height, s=200, c='r', marker='*')
# 绘制曲线图
plt.plot(x1, ys0, color='darkgoldenrod', linestyle=':')
plt.title('2.1.a  Plot height as a function of mean temperature')
plt.xlabel('Mean air temperature (C)')
plt.ylabel('Height (m)')
plt.grid()


# 2.1.b
z_H = 0.02 * 0.15
d = 0.6 * 0.15
x2 = np.linspace(31, 38, 27)
equation = np.zeros(len(height))
for i in range(len(height)):
    equation[i] = math.log((height[i] - d) / z_H, math.e)
# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model1 = make_interp_spline(mean_air_temperature, equation)
ys1 = model1(x2)
# 开始绘图
plt.subplot(2,2,2)
# 绘制散点图
plt.scatter(mean_air_temperature, equation, s=200, c='peachpuff', marker='X')
# 绘制曲线图
plt.plot(x2, ys1, color='cyan', linestyle='-.')
plt.title('2.1.b  Plot {} as a function of mean temperature'.format(r'$ln\left [ \left ( z-d \right ) /z_{H}\right ]$'))
plt.xlabel('Mean air temperature (C)')
plt.ylabel(r'$ln\left [ \left ( z-d \right ) /z_{H}\right ]$')
plt.grid()


# 2.1.c
x2 = np.linspace(31, 38, 27)
equation = np.zeros(len(height))
for i in range(len(height)):
    equation[i] = math.log((height[i] - d) / z_H, math.e)
# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model1 = make_interp_spline(mean_air_temperature, equation)
ys1 = model1(x2)
# 开始绘图
plt.subplot(2,2,3)
# 绘制散点图
plt.scatter(mean_air_temperature, equation, s=200, c='violet', marker='P')
# print(point)
# 绘制曲线图
plt.plot(x2, ys1, color='tomato', linestyle='-')
plt.axhline(0, color='r', linestyle='--')
plt.axvline(37.988709570430, color='r', linestyle='--')
plt.scatter(37.988709570430, 5e-11, s=200, c='g', marker='o', linestyle='-', label=r'$ln\left [ \left ( z-d \right ) /z_{H}\right ]=0$')
plt.title('2.1.c  From the plot in b, find the aerodynamic surface temperature')
plt.xlabel('Mean air temperature (C)')
plt.ylabel(r'$ln\left [ \left ( z-d \right ) /z_{H}\right ]$')
plt.text(37.988709570430, 0, '(37.988709570430,0)', fontsize=20, fontstyle='italic')
plt.legend()
plt.grid()

plt.show()


# 2.1.d
z_H = 0.02 * 0.15
d = 0.6 * 0.15
T0 = 37.988709570430
H = np.zeros(len(height))
print("Answer for 2.1.d:")
for i in range(len(height)):
    H[i] = ((0.4 * 0.2 * 1200) * (T0 - mean_air_temperature[i])) / math.log((height[i] - d ) / z_H)
    print(f"When height = {height[i]:.1f} , Mean air temperature = {mean_air_temperature[i]:.2f}, then the sensible heat flux ={H[i]:.4f}")

