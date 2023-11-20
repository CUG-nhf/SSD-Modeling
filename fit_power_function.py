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
	rbers, ubers= [], []

# '-v', label='Proposed'
	rber = [1.26e-2,1.34e-2,1.39e-2,1.44e-2,1.51e-2,1.61e-2,1.72e-2,1.82e-2]
	uber = [3e-10,4e-8,5e-7,5e-6,6e-5,6e-4,3e-3,8e-3]
	rbers.append(rber)
	ubers.append(uber)
# '-*', label='ISCAS\'21'
	rber = [1e-2,1.12e-2,1.4e-2,1.51e-2,1.59e-2,1.68e-2,1.82e-2]
	uber = [1e-5,2e-5,1.5e-4,4e-4,2e-3,4e-3,9e-3]
	rbers.append(rber)
	ubers.append(uber)
# '-x', label='TCAS-II\'18'
	rber = [0.76e-2, 0.9e-2, 1.0e-2, 1.1e-2, 1.2e-2]
	uber = [1e-11,3e-7,5e-5,2e-3,9e-3]
	rbers.append(rber)
	ubers.append(uber)
# '-^', label='TCAS-I\'17
	rber = [1.28e-2,1.36e-2,1.45e-2,1.55e-2,1.65e-2]
	uber = [6e-6,1.5e-4,1.5e-3,6e-3,9e-3]
	rbers.append(rber)
	ubers.append(uber)
# '-o', label='TVLSI\'16'
	rber = [1.05e-2,1.13e-2,1.21e-2,1.3e-2,1.38e-2,1.47e-2,1.67e-2]
	uber = [3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3]
	rbers.append(rber)
	ubers.append(uber)
	labels = ['Proposed', 'ISCAS\'21', 'TCAS-II\'18', 'TCAS-I\'17', 'TVLSI\'16']
	colors = ['red', 'brown', 'green', 'black', 'blue']
	# labels = ['LDPC(2KB,0.90-rate)', 'LDPC(8KB,0.96-rate)', 'LDPC(4KB,0.90-rate)']
	# colors = ['green', 'purple', 'blue']
	fits(rbers, ubers, labels, colors)
	

