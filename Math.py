import math

# 计算柏松概率
def Possion(Lambda, n, t):
    return math.pow(Lambda * t, n) * math.exp(-Lambda * t) / math.factorial(n)



# 计算累积二项分布概率
def Binomial(N, E, R):

	p = 0.0
	for n in range(E + 1, N + 1):
		t = math.factorial(N) / (math.factorial(n) * math.factorial(N - n))
		p +=  t * pow(R, n) * pow(1 - R, N - n)
	
	return p


if __name__ == '__main__':
	
	page_size = 4 * 1024 * 8
	page_error_rate = 0.0001
	page_error_bit = int(page_size * page_error_rate)
	print(page_error_bit)

	N = 20
	E = 8
	R = 1E-4

	print(Binomial(N, E, R))

"""
把 ECC 加入到 page2block 的柏松模型的难度：
	难点1：对上层来说读取是以page为单位的，一般page_size = 4kB = 32768 b，比特数太大，组合数不好算
	难点2：如果把对page的读取分为多个小读取，每个都用ECC，那么我需要知道读取长度、ECC纠错长度、RBER
		  才能去算UBER，但是Uncorrectable Error可以直接从SMART中读到，不需要计算啊
"""