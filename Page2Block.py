import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Possion import Possion3
from Binomial import Binomial

"""
有关参数的思考：
	在原文中, lambda = AFR / (24*365) * N, 表示有N个SSD的集群在单位时间内发生故障的概率
	而本文中，我们考察的“时间”单位是 PE次数
	所以 lambda应该表示: 有npage个页的block在单位PE次数时发生故障的概率
	疑惑：事实上，不同的PE次数时，page error rate其实是不同的，应为擦写越多，故障率越高
	所以本文用固定的page error rate，去看PE对block故障率的影响是否合理
"""

npage = 1152
nblock = 990
nplane = 2
ndie = 2
nchip = 2
nchannel =2
PE = [1000, 5000, 7000, 10000]
page_error_rate = [0.0001, 0.00015, 0.0003, 0.0006]

def pro1():
	lbd = page_error_rate[0] * npage / PE[0]
	p1_any = [1 - Possion3(lbd, 0, p) for p in PE]

	print("在page error rate=%f 时，度量 PE 对block故障率的影响" % lbd)
	print('PE:', PE)
	print ('Block error rate:', p1_any)

	plt.plot(PE, p1_any, 'o-', label = 'page error rate=%f'% lbd)
	plt.xlabel("PE")
	plt.ylabel("Block error rate")
	plt.legend(loc ='best')
	plt.show()


def pro2():
	pe = PE[0]
	PER = np.array(page_error_rate) / pe * npage
	p1_any = [1 - Possion3(l, 0, pe) for l in PER]

	print("在PE=%d时，度量page error rate对block故障率的影响" % pe)
	print('page error rate:', page_error_rate)
	print ('Block error rate:', p1_any)

	plt.plot(PER, p1_any, 'o-', label = 'PE=%d'% pe)
	plt.xlabel("page error rate")
	plt.ylabel("Block error rate")
	plt.legend(loc ='best')
	plt.show()


def page2block(show = True):
	Lambda = np.array(page_error_rate) * npage / np.array(PE)
	p1_any = [1 - Possion3(Lambda[i], 0, PE[i]) for i in range(len(PE))]
	
	if not show:
		return p1_any

	print('PE:', PE)
	print('page error rate:', page_error_rate)
	print('Block error rate', p1_any)

	fig = plt.figure()
	ax1 = plt.axes(projection = '3d')
	ax1.plot3D(PE, page_error_rate, p1_any, 'o-')
	ax1.set_xlabel('PE')
	ax1.set_ylabel('page error rate')
	ax1.set_zlabel('Block error rate')
	plt.show()
	"""
	http://www.ssdfans.com/?p=8074 
	这篇文章提到了MLC最大擦写次数是几千到几万，
	故本函数得到的 block error rate 可能是正确的
	"""


def block2plane(show = True):
	block_error_rate = page2block(show=False)
	Lambda = np.array(block_error_rate) * nblock / np.array(PE)
	# print(Lambda)
	p1_any = [1 - Possion3(Lambda[i], 0, PE[i]) for i in range(len(PE))]
	
	if not show:
		return p1_any

	print('PE:', PE)
	print('block error rate:', block_error_rate)
	print('plane error rate', p1_any)

	fig = plt.figure()
	ax1 = plt.axes(projection = '3d')
	ax1.plot3D(PE, block_error_rate, p1_any, 'o-')
	ax1.set_xlabel('PE')
	ax1.set_ylabel('block error rate')
	ax1.set_zlabel('plane error rate')
	plt.show()

# block2plane()

page2block()