import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.txt', delimiter='\t')

a1 = np.zeros((999, 11))
a2 = np.zeros((999, 11))
i = 0
j = 0

for rows in data[1:, :]:
    if 1 == rows[0]:
        a1[i, :] = rows
        i += 1
    if 2 == rows[0]:
        a2[j, :] = rows
        j += 1

a1 = a1[:i, :]
a2 = a2[:j, :]
for i in range(1, 10):
    for j in range(2, 11):
        u1 = u2 = v1 = v2 = np.zeros((999, 1))
        if j > i:
            u1 = a1[:, i]
            v1 = a1[:, j]
            u2 = a2[:, i]
            v2 = a2[:, j]

            plt.scatter(v1, u1, c='r', label='Label 1')
            plt.scatter(v2, u2, c='b', label='Label 2')

            plt.xlabel('Feature %d' % i)
            plt.ylabel('Feature %d' % j)
            plt.title('Feature %d vs Feature %d' % (j, i))
            plt.legend()
            plt.show()

# Feature 2 and Feature 1 best classifies the data
