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
	
	if needLog:
		plt.xlabel("$log_{10}(RBER)$")
		plt.ylabel("$log_{10}(UBER)$")
	else:
		plt.xlabel("RBER")
		plt.ylabel("UBER")
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

	rber = [0.75e-2, 0.83e-2, 0.89e-2, 1.0e-2, 1.18e-2, 1.342e-2, 1.5e-2, 1.75e-2, 1.94e-2]
	uber = [6.579e-7, 5.921e-6, 1.711e-5, 5.789e-5, 7.763e-5,7.752e-5, 7.742e-5, 7.732e-5, 7.732e-5]

	fit(np.array(rber), np.array(uber))

