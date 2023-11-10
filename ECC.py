from scipy.stats import binom
import matplotlib.pyplot as plt
from math import log10
import decimal
from decimal import Decimal
import numpy as np
from tqdm import tqdm
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")

decimal.getcontext().prec = 2000

def fun1():
	N = 2 * 1024 * 8
	rber = np.logspace(-3, -2, 11, 10) 
	num_E = [820] 	# Number of correctable bits

	for E in num_E:
		uber = np.float64([1 - binom.cdf(E, N, r) for r in rber]) / np.float64(N)
		
		plt.loglog(rber, uber, '-', label='{}b/{}b'.format(E, N))

	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.savefig('picture/uber-rber-' + str(formatted_datetime))
	# plt.show()


def fun2():
	# N = 256
	#rber = np.logspace(-7, -2, 51, 10)
	# number_E = [1, 2, 3]
	N = 2 * 1024 * 8
	rber = np.logspace(-3, -2, 11, 10)
	number_E = [820]

	Com = {}
	for E in number_E:
		uber = []
		for r in rber:
			p, R = Decimal(0), Decimal(r)
			for n in range(0, E + 1):
				# 计算组合数
				if n in Com.keys():
					a, b = Com[n][0], Com[n][1]
				else:
					a, b = Decimal(1), Decimal(1)
					for i in range(n):
						a *= (N - i)
						b *= (i + 1) 
					Com[n] = [a, b]
				# 计算次方
				c, d = Decimal(1), Decimal(1)
				for i in range(n):
					c *= R
				for i in range(N - n):
					d *= (1 - R)
				# 计算二项分布概率
				p +=  a / b * c * d
			uber.append(1 - p)

		plt.loglog(rber, uber, '-', label='{}b/{}b'.format(E, N))
	
	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.savefig('picture/uber-rber-' + formatted_datetime)
	# plt.show()

fun1()