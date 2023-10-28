import math

# 使用二项分布计算 UBER

def Binomial(N, E, R):
	"""
	N:  总比特数
	E： ECC 可纠正比特数
	R： RBER
	"""
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

	N = 512
	E = 8
	R = 1E-4

	print(Binomial(N, E, R))
