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

N = 2 * 1024 * 8
code_rate = 0.1  # 纠错码的比例
rber = [0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02]
number_E = [int(N * code_rate)]

# N = 128
# rber = np.logspace(-7, -2, 51, 10)
# number_E = [1, 2, 3]


def fun1():
	for E in number_E:
		uber = np.float64([1 - binom.cdf(E, N, r) for r in rber]) / np.float64(N)
		
		plt.loglog(rber, uber, '-', label='{}b/{}b'.format(E, N))

	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.savefig('picture/{}b-{}b-binom-'.format(E, N) + formatted_datetime)
	# plt.show()


def fun2():
	Com = {}
	for E in number_E:
		uber = []
		for r in rber:
			p, R = Decimal(0), Decimal(r)
			for n in range(0, E + 1):
				# 计算组合数
				if n in Com.keys():
					e = Com[n]
				else:
					a, b = Decimal(1), Decimal(1)
					for i in range(n):
						a *= (N - i)
						b *= (i + 1) 
					e = a / b
					Com[n] = e
				c, d = Decimal(1), Decimal(1)
				for i in range(n):
					c *= R
				for i in range(N - n):
					d *= (1 - R)
				# 计算二项分布概率
				p +=  e * c * d
			uber.append((1 - p) / N)

		plt.loglog(rber, uber, '-', label='{}b/{}b'.format(E, N))
	
	plt.xlabel("RBER")
	plt.ylabel("UBER")
	plt.legend(loc ='best')
	plt.savefig('picture/{}b-{}b-decimal-'.format(E, N) + formatted_datetime)
	# plt.show()


# 1. 已经通过实验验证 fun1 与 fun2 是等价的
# 2. 但是 N 较大时，通过fun2计算得到的uber非常小，
#    几乎与论文中的数字天差地别，因此论文中的UBER应该是模拟器直接输出的的，而不是公式计算
# 3. 模拟的UBER远大于理论计算值，可能是在现实情况下，多个因素的综合导致UBER增加

fun2()