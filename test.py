import numpy as np
import matplotlib.pyplot as plt

def linear_interpolation(x_values, y_values, x):
    """
    使用线性插值法估计在给定 x 处的函数值。

    参数：
    - x_values: 数据点的 x 坐标
    - y_values: 数据点的 y 坐标
    - x: 要估计函数值的位置
    """
    # 寻找 x 所在的区间
    idx = np.searchsorted(x_values, x)

    # 确保 x 不超出数据范围
    idx = np.clip(idx, 1, len(x_values) - 1)

    # 计算线性插值
    x0, x1 = x_values[idx - 1], x_values[idx]
    y0, y1 = y_values[idx - 1], y_values[idx]
    y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    return y

def newton_interpolation(x_values, y_values, x):
    n = len(x_values)
    coefficients = np.zeros(n)
    f = np.copy(y_values)

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            f[j] = (f[j] - f[j - 1]) / (x_values[j] - x_values[j - i])

    for i in range(n):
        coefficients[i] = f[i]

    result = coefficients[0]
    product_term = 1

    for i in range(1, n):
        product_term *= (x - x_values[i - 1])
        result += coefficients[i] * product_term

    return result

def plot_newton_interpolation(x_values, y_values, x_to_estimate):
    # 计算插值结果
    y_interpolated = [newton_interpolation(x_values, y_values, xi) for xi in x_to_estimate]

    # 绘制原数据点
    plt.scatter(x_values, y_values, color='blue', label='Data Points')

    # 绘制插值结果
    plt.plot(x_to_estimate, y_interpolated, color='red', label='Newton Interpolation')

    plt.title('Newton Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# 示例
# x_values = np.array([0.76e-2, 0.9e-2, 1.0e-2, 1.1e-2, 1.2e-2])
# y_values = np.array([1e-11,3e-7,5e-5,2e-3,9e-3])

# # 生成一系列 x 以便绘制插值结果
# x_to_estimate = np.linspace(min(x_values), max(x_values), 50)

# # 绘制牛顿插值结果和原数据点
# plot_newton_interpolation(x_values, y_values, x_to_estimate)
