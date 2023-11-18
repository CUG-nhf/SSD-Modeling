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
	plt.show()


def fig3():
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
	plt.show()


def fig2():
	#https://www.flashmemorysummit.com/English/Collaterals/Proceedings/2013/20130814_E22_YangJ.pd
	rber = [5e-3, 6e-3, 7e-3, 8e-3, 9e-3, 1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	uber = [9e-16, 1e-13, 6e-11, 8e-9,2e-7,5e-6,9e-5,1e-4,1e-4,1e-4,1e-4]
	plt.plot(rber, uber, '-o', label='hre25')

	rber = [8e-3,9e-3,1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2, 2e-2]
	uber = [3e-11,2e-9,2e-7,2e-5,9e-5,1e-4,1e-4,1e-4]
	plt.plot(rber, uber, '-x', label='hre20')

	rber = [8e-3,9e-3,1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	uber = [8e-14,9e-12,2e-9,1e-6,7e-5,1e-4,1e-4,1e-4]
	plt.plot(rber, uber, '-x', label='hre15')

	rber = [1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	uber = [1e-11,8e-8,8e-6,9e-5,1e-4,1e-4]
	plt.plot(rber, uber, '-^', label='hre10')

	rber = [1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2e-2]
	uber = [5e-13,1e-9,1e-6,5e-5,9e-5,1e-4]
	plt.plot(rber, uber, '-s', label='hre5')

	rber = [1e-2,1.2e-2,1.4e-2,1.6e-2,1.8e-2,2.1e-2]
	uber = [1e-16,9e-12,9e-8,9e-6,1e-4,1e-4]
	plt.plot(rber, uber, '-+', label='hre0')

	plt.xlim(0.001, 0.022)
	plt.ylim(1e-16, 1e-3)
	plt.yscale('log')
	plt.xscale('log')
	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.title('TLC-LDPC Strong-Error simulation')
	plt.show()


def fig4():
	#An energy-optimized (37840, 34320) symmetric BC-BCH decoder for healthy mobile storages
	rber = [16.8,17.3,17.7,18.5,19.3]
	uber = [2.9e-7,4.6e-5,2.9e-4,1.5e-3,6.2e-3]
	plt.plot(rber, uber, '-Dg', label='LDPC(2KB,0.90-rate)')

	rber = [16.3,16.8]
	uber = [1e-12,2.9e-7]
	plt.plot(rber, uber, '--g')

	rber = [4.53,5,5.27,5.52]
	uber = [7e-8,8e-6,1.7e-4,3e-3]
	plt.plot(rber, uber, '->y', label='LDPC(8KB,0.96-rate)')

	rber = [3.75, 4.53]
	uber = [1e-12,7e-8]
	plt.plot(rber, uber, '--y')


	rber = [17.3,17.7,18.1,18.5,18.9,19.7]
	uber = [2.9e-11,1e-7,3e-6,6e-5,5.6e-4,6.7e-3]
	plt.plot(rber, uber, '-<b', label='LDPC(4KB,0.90-rate)')

	rber = [17.3,17.3]
	uber = [1e-12,2.9e-11]
	plt.plot(rber, uber, '--b')

	plt.xlim(3, 20)
	plt.ylim(1e-12, 1e-2)
	plt.yscale('log')
	# plt.xscale('log')
	plt.xlabel("RBER($10^{-3}$)")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.grid('on',which='both')
	plt.title('SD ECCs')
	plt.show()

fig3()


