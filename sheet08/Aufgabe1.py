import numpy as np
np.random.seed(42)
data = np.random.rand(100, 2)

print(data.size)
print(data[0, 1])
print(data[-1])
print(data[10])
print(data[51:60, 0])
print(np.mean(data[51:99, 0]))