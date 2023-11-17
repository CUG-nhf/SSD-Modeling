import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


# 定义幂函数
def power_law(x, a, b, c, d, e):
		return  a*pow(x, 3) + b*pow(x, 2) + c*pow(x, 1) + d + e*pow(x, 5)

def fit1():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		return a*pow(x, 3) + b*pow(x, 2) + c*pow(x, 1) + d

	# 原数据
	rber = [0.75e-2, 0.83e-2, 0.89e-2, 1.0e-2, 1.18e-2, 1.342e-2, 1.5e-2, 1.75e-2, 1.94e-2]
	uber = [6.579e-7, 5.921e-6, 1.711e-5, 5.789e-5, 7.763e-5,7.752e-5, 7.742e-5, 7.732e-5, 7.732e-5]
	
	# 使用三次样条插值法增加数据点
	cs = CubicSpline(rber, uber)
	x_fit = np.linspace(rber[0], rber[-1], 50)
	y_fit = cs(x_fit)
	plt.plot(x_fit, y_fit, label='interpolated',  color='green')

	# 使用使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, x_fit, y_fit)
	print(params)
	a, b, c, d = params

	# 生成拟合的曲线
	y_fit = power_law(x_fit, a, b, c, d)
	
	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label='fit interpolated', color='red')

	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.yscale('log')
	plt.xscale('log')
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()

def fit_log(rber, uber):
	
	# 原数据 x, y 取log
	rber = np.log10(rber)
	uber = np.log10(uber)
	plt.scatter(rber, uber, label='Raw Data')
	x_fit = np.linspace(rber[0], rber[-1], 50)

	# 基于原数据 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)
	print(params)
	a, b, c, d, e = params
	y_fit = power_law(x_fit, a, b, c, d, e)
	plt.plot(x_fit, y_fit, label='fit raw data', color='red')

	# 使用三次样条插值法增加数据点
	cs = CubicSpline(rber, uber)
	y_fit = cs(x_fit)
	plt.plot(x_fit, y_fit, label='interpolated',  color='green')
	params, covariance = curve_fit(power_law, x_fit, y_fit)
	print(params)
	a, b, c, d, e = params
	y_fit = power_law(x_fit, a, b, c, d, e)
	plt.plot(x_fit, y_fit, label='fit interpolated', color='yellow')
	
	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
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


def fit2_log():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		return  a*pow(x, 3) + b*pow(x, 2) + c*pow(x,1) + d
 
	# 原数据 x, y 取log
	rber = np.array([1.05e-2,1.13e-2,1.21e-2,1.3e-2,1.38e-2,1.47e-2,1.67e-2])
	uber = np.array([3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3])
	rber = np.log10(rber)
	uber = np.log10(uber)
	print(rber)
	print(uber)

	# 使用三次样条插值法增加数据点
	# cs = CubicSpline(rber, uber)
	x_fit = np.linspace(rber[0], rber[-1], 50)
	# y_fit = cs(x_fit)
	# plt.plot(x_fit, y_fit, label='interpolated',  color='green')

	# 使用使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)
	print(params)
	a, b, c, d = params

	# 生成拟合的曲线
	y_fit = power_law(x_fit, a, b, c, d)
	
	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label='fit raw data', color='red')

	# 使用三次样条插值法增加数据点
	cs = CubicSpline(rber, uber)
	y_fit = cs(x_fit)
	plt.plot(x_fit, y_fit, label='interpolated',  color='green')
	params, covariance = curve_fit(power_law, x_fit, y_fit)
	print(params)
	a, b, c, d = params
	y_fit = power_law(x_fit, a, b, c, d)
	plt.plot(x_fit, y_fit, label='fit interpolated', color='yellow')

	
	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()


def fit2_1():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		# return a*pow(x,4) + b*pow(x, 2) + c*pow(x, 1) + d
		return a*pow(x+b,2.5) + c*pow(x, 1) + d
	
	# 原数据
	# rber = [1,1.12,1.4,1.51,1.59,1.68,1.82]
	# uber = [1e-5,2e-5,1.5e-4,4e-4,2e-3,4e-3,9e-3]
	rber = [1.05,1.13,1.21,1.3,1.38,1.47,1.67]
	uber = [3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3]
	# 使用 curve_fit 拟合幂函数ss
	params, covariance = curve_fit(power_law, rber[2:], uber[2:])
	print(params)

	a, b, c, d = params

	# 生成拟合的曲线
	x_fit = np.linspace(0.9, 1.9, 50)
	y_fit = power_law(x_fit, a, b, c, d)

	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label=f'Fit', color='red')

	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.yscale('log')
	plt.legend(loc ='best')
	plt.title('')
	plt.grid('on',which='both')
	plt.show()

def fit3():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		# return a*pow(x+b,2)+c*pow(x,1) + d
		return a*pow(x,3) + b*pow(x,2) +c*pow(x,1) + d

	# 原数据
	# rber = [5e-3, 6e-3, 7e-3, 8e-3, 9e-3, 1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	rber = [5, 6, 7, 8, 9, 10,12,14]
	# uber = [9e-16, 1e-13, 6e-11, 8e-9,2e-7,5e-6,9e-5,1e-4,1e-4,1e-4,1e-4]
	uber = [9e-10, 1e-3, 6e-5, 8e-3,2e-1,5,90,100]
	# 使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)

	print(params)

	a, b, c, d = params

	# 生成拟合的曲线
	x_fit = np.linspace(4, 15, 50)
	y_fit = power_law(x_fit, a, b, c, d)

	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label=f'Fit', color='red')

	plt.xlabel("RBER(%)")
	plt.ylabel("UBER($10^{-6}$)")
	# plt.yscale('log')
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()

def fit4():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		return a*pow(x,3) + b*pow(x, 2) + c*pow(x,1) + d

	# 原数据
	rber = [1.68,1.73,1.77,1.85,1.93]
	uber = [2.9e-7,4.6e-5,2.9e-4,1.5e-3,6.2e-3]
	
	from test import linear_interpolation
	x_to_estimate = np.linspace(min(rber), max(rber), 50)
	y_interpolated = [linear_interpolation(rber, uber, xi) for xi in x_to_estimate]
	plt.plot(x_to_estimate, y_interpolated, color='green')
	params1, covariance1 = curve_fit(power_law, rber, uber)
	a, b, c, d = params1
	print(params1)
	# 生成拟合的曲线
	x_fit = np.linspace(1.6, 2, 100)
	y_fit = power_law(x_fit, a, b, c, d)
	plt.plot(x_fit, y_fit, color='green', label='fitting raw data')

	plt.plot(x_to_estimate, y_interpolated, color='yellow', label='interpolated')

	# 使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, x_to_estimate, y_interpolated)

	print(params)

	a, b, c, d = params

	# 生成拟合的曲线
	x_fit = np.linspace(1.6, 2, 100)
	y_fit = power_law(x_fit, a, b, c, d)

	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label=f'fitting interpolated', color='red')

	plt.xlabel("RBER($10^{-2}$)")
	plt.ylabel("UBER)")
	plt.yscale('log')
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.title("fig4-LDPC(2KB,0.90-rate)")
	plt.show()


rber = [1.68,1.73,1.77,1.85,1.93]
uber = [2.9e-7,4.6e-5,2.9e-4,1.5e-3,6.2e-3]

fit_log(rber, uber)