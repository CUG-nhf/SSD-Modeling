import math
import numpy as  np


def Com(n ,m):
	return math.factorial(n) / ( math.factorial(m) * math.factorial(n - m) )


page_error_rate = [0.0001, 0.00015, 0.0003, 0.0006]
npage = 1152
nblock = 990
nplane = 2
ndie = 2
nchip = 2
nchannel =2

p = 1 - pow((1 - np.array(page_error_rate)), npage)
print(p)

p = 1 - pow((1 - p), nblock)
print(p)
