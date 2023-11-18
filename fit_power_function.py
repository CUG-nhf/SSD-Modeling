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

	# Plot raw data and fitted curve
	plt.scatter(rber, uber, label='Raw Data')
	plt.plot(x_fit, y_fit, label='fitted curve', color='red')
	
	plt.xlabel("$log_{10}(RBER)$")
	plt.ylabel("$log_{10}(UBER)$")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.show()

	
if	__name__ == '__main__':
	
	rber = [0.76e-2, 0.9e-2, 1.0e-2, 1.1e-2, 1.2e-2]
	uber = [1e-11,3e-7,5e-5,2e-3,9e-3]
	fit(rber, uber)

