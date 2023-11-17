import numpy as np
import matplotlib.pyplot as plt

rber = [1.05e-2,1.13e-2,1.21e-2,1.3e-2,1.38e-2,1.47e-2,1.67e-2]
uber = [3e-10,1e-7,7e-6,2e-4,2e-3,6e-3,8e-3]

plt.plot(rber, uber)
plt.xlabel('rber')
plt.ylabel('uber')
plt.xlim(1.05e-2, 1.67e-2)
plt.ylim(3e-10, 8e-3)
plt.yscale('log')
plt.xscale('log')
plt.show()