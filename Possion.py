import math

# 计算柏松概率

def Possion3(Lambda, n, t):
    return math.pow(Lambda * t, n) * math.exp(-Lambda * t) / math.factorial(n)


def Possion2(Lambda, k):
    return math.pow(Lambda, k) * math.exp(-Lambda) / math.factorial(k)