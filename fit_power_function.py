import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Define power function
def power_law(x, a, b, c, d):
		return  a*pow(x, 3) + b*pow(x, 2) + c*pow(x, 1) + d

# fit power function
def fit(rber, uber, needLog=True):
	"""
	rber: raw RBER data from the paper
	uber: raw UBER data from the paper
	needLog: whether need taking logarithm of raw data
	"""

	# logarithm of raw data
	if needLog:
		rber = np.log10(rber)
		uber = np.log10(uber)

	# Using curve_fit() to fit the power function
	params, covariance = curve_fit(power_law, rber, uber)
	print('The coefficients of the fitted function are:\n', params)

	# Generate the fitted curve
	x_fit = np.linspace(rber[0], rber[-1], 50)
	a, b, c, d = params
	y_fit = power_law(x_fit, a, b, c, d)
	plt.plot(x_fit, y_fit, label='fitted curve')
	# Plot raw data and fitted curve
	plt.scatter(rber, uber, label='Raw Data')
	
	
	plt.xlabel("$log_{10}(RBER)$")
	plt.ylabel("$log_{10}(UBER)$")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()


# fit some power functions
def fits(rbers, ubers, labels, colors, needLog=True):
	"""
	rbers: list of the raw RBER data from the paper
	ubers: list of theraw UBER data from the paper
	needLog: whether need taking logarithm of raw data
	"""
	for i in range(len(rbers)):
		rber, uber = rbers[i], ubers[i]
		# logarithm of raw data
		if needLog:
			rber = np.log10(rber)
			uber = np.log10(uber)

		# Using curve_fit() to fit the power function
		params, covariance = curve_fit(power_law, rber, uber)
		print('The coefficients of the fitted function are:\n', params)

		# Generate the fitted curve
		x_fit = np.linspace(rber[0], rber[-1], 50)
		a, b, c, d = params
		y_fit = power_law(x_fit, a, b, c, d)
		
		# Plot raw data and fitted curve
		plt.scatter(rber, uber, color=colors[i])
		plt.plot(x_fit, y_fit, color=colors[i], label=labels[i])
	
	
	plt.xlabel("$log_{10}(RBER)$")
	plt.ylabel("$log_{10}(UBER)$")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()


if	__name__ == '__main__':
	# rbers, ubers= [], []

	# labels = ['LDPC(2KB,0.90-rate)', 'LDPC(8KB,0.96-rate)', 'LDPC(4KB,0.90-rate)']
	# colors = ['green', 'purple', 'blue']
	# fits(rbers, ubers, labels, colors)
	
	rber = [17.3e-3,17.7e-3,18.1e-3,18.5e-3,18.9e-3,19.7e-3]
	uber = [2.9e-11,1e-7,3e-6,6e-5,5.6e-4,6.7e-3]

	fit(rber, uber)

