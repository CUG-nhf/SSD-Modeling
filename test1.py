import matplotlib.pyplot as plt
import numpy as np

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
	plt.grid('on',which='both')
	# plt.savefig('picture/{}b-{}b-binom-'.format(E, N) + formatted_datetime)
	plt.show()

def fig2():
	#A 38.64-Gb/s Large-CPM 2-KB LDPC Decoder Implementation for nand Flash Memories
	
	rber = [1.26,1.34,1.39,1.44,1.51,1.61,1.72,1.82]
	uber = [3e-10,4e-8,5e-7,5e-6,6e-5,6e-4,3e-3,8e-3]
	plt.plot(rber, uber, '-v', label='Proposed')

	rber = [1,1.12,1.4,1.51,1.59,1.68,1.82]
	uber = [1e-5,2e-5,1.5e-4,4e-4,2e-3,4e-3,9e-3]
	plt.plot(rber, uber, '-*', label='ISCAS\'21')

	rber = [0.76, 0.9, 1.0, 1.1, 1.2]
	uber = [1e-11,3e-7,5e-5,2e-3,9e-3]
	plt.plot(rber, uber, '-x', label='TCAS-II\'18')

	rber = [1.28,1.36,1.45,1.55,1.65]
	uber = [6e-6,1.5e-4,1.5e-3,6e-3,9e-3]
	plt.plot(rber, uber, '-^', label='TCAS-I\'17')

	rber = [1.05,1.13,1.21,1.3,1.38,1.47,1.67]
	uber = [3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3]
	plt.plot(rber, uber, '-o', label='TVLSI\'16')

	plt.xlim(0.7, 1.9)
	plt.ylim(5e-12, 1e-1)
	plt.yscale('log')
	plt.xlabel("RBER(%)")
	plt.ylabel("UBER(log10)")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.title('2KB LDPC')
	# plt.savefig('picture/{}b-{}b-binom-'.format(E, N) + formatted_datetime)
	plt.show()


fig2()


