import numpy as np
import matplotlib.pyplot as plt

rber = [1.05e-2,1.13e-2,1.21e-2,1.3e-2,1.38e-2,1.47e-2,1.67e-2]
uber = [3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3]

plt.plot(rber, uber)
plt.xlabel('rber')
plt.ylabel('uber')
plt.xlim(1.05e-2, 1.67e-2)
plt.ylim(3e-10, 8e-3)
plt.yscale('log')
plt.xscale('log')
plt.show()


def fit2():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		return  a*pow(x, 3) + b*pow(x, 2) + c*pow(x,1) + d
 
	# 原数据 x, y 都乘e6
	rber = [1.05e4,1.13e4,1.21e4,1.3e4,1.38e4,1.47e4,1.67e4]
	uber = [3e-4,1e-1,7,2e3,2e3,6e3,8e3]
	
	# 使用三次样条插值法增加数据点
	cs = CubicSpline(rber, uber)
	x_fit = np.linspace(rber[0], rber[-1], 50)
	y_fit = cs(x_fit)
	# plt.plot(x_fit, y_fit, label='interpolated',  color='green')

	# 使用使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)
	print(params)
	a, b, c, d = params

	# 生成拟合的曲线
	y_fit = power_law(x_fit, a, b, c, d)
	
	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label='fit interpolated', color='red')

	plt.xlabel("RBER")
	plt.ylabel("UBER")
	# plt.yscale('log')
	# plt.xscale('log')
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()