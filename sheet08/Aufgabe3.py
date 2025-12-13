import numpy as np
import matplotlib.pyplot as plt

data = np.zeros((10, 10))

data[1:7, 3] = 1

data[2, 5:7] = 1

data[6, 5:7] = 1

plt.imshow(data.T, origin='lower')
plt.colorbar()
plt.show()