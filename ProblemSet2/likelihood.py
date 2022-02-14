import numpy as np
import matplotlib.pyplot as plt

n=100
num_ones=60
theta_values = np.linspace(0, 1.0, num=101)

plt.plot(theta_values, [pow(theta, num_ones) * pow(1 - theta, n-num_ones) for theta in theta_values], 'x')
plt.xlabel("theta")
plt.ylabel("likelihood")
# x = [0.6]
# y = [0.0011943936]
# plt.plot(x, y, marker='o')
plt.savefig("C:/Users/bonni/OneDrive/Desktop/CSM146/ProblemSets/ProblemSet2/3d-likelihood-n100-ones60.png")
plt.show()
