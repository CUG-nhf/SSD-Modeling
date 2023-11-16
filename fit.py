import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def fit1():
	# 定义幂函数
	def power_law(x, a, b, c, d):
		return a*pow(x,3) + b*pow(x, 1.5) + c*pow(x,1) + d
		# [ 7.33820523e-05 -1.29416212e-03  1.87978880e-03 -6.09156463e-04]

	# 原数据
	rber = [0.75, 0.83, 0.89, 1.0, 1.18, 1.342, 1.5, 1.75, 1.94]
	uber = [6.579e-7, 5.921e-6, 1.711e-5, 5.789e-5, 7.763e-5,7.752e-5, 7.742e-5, 7.732e-5, 7.732e-5]

	# 使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)

	print(params)

	a, b, c, d = params

	# 生成拟合的曲线
	x_fit = np.linspace(0.7, 2, 100)
	y_fit = power_law(x_fit, a, b, c, d)

	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label=f'Fit', color='red')

	plt.xlabel("RBER($10^{-2}$)")
	plt.ylabel("UBERs)")
	plt.yscale('log')
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.title("fig1-red line")
	plt.show()


def fit2():
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

	plt.xlabel("RBER(%)")
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
		return a*pow(x,4) + b*pow(x,3) +c*pow(x,1) + d

	# 原数据
	# rber = [5e-3, 6e-3, 7e-3, 8e-3, 9e-3, 1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	rber = [5, 6, 7, 8, 9, 10,12,14,16,18,20]
	uber = [9e-16, 1e-13, 6e-11, 8e-9,2e-7,5e-6,9e-5,1e-4,1e-4,1e-4,1e-4]
	# 使用 curve_fit 拟合幂函数
	params, covariance = curve_fit(power_law, rber, uber)

	print(params)

	a, b, c, d = params

	# 生成拟合的曲线
	x_fit = np.linspace(4, 21, 50)
	y_fit = power_law(x_fit, a, b, c, d)

	# 绘制原始数据和拟合曲线
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label=f'Fit', color='red')

	plt.xlabel("RBER(%)")
	plt.ylabel("UBERs")
	plt.yscale('log')
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

fit3()