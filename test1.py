import matplotlib.pyplot as plt

def fig1():
	#ALCod: Adaptive LDPC Coding for 3D NAND Flash Memory Using Inter-Layer RBER Variation
	rber = [0.75, 0.83, 0.89, 1.0, 1.18, 1.342, 1.5, 1.75, 1.94]
	uber = [6.579e-7, 5.921e-6, 1.711e-5, 5.789e-5, 7.763e-5, 
	  	7.752e-5, 7.742e-5, 7.732e-5, 7.732e-5]

	plt.plot(rber, uber, '-or', label='emulation, 3D TLC')

	plt.xlim(0, 2.0)
	plt.ylim(1e-7, 1e-4)
	plt.yscale('log')
	plt.xlabel("RBER($10^{-2}$)")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	# plt.savefig('picture/{}b-{}b-binom-'.format(E, N) + formatted_datetime)
	plt.show()

fig1()
