import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from lmfit import Model, Parameters

messdatenDataPath = r"sheet09\data.txt"

messdatenData = pd.read_csv(messdatenDataPath, delimiter=',', decimal='.', dtype=float)

x = messdatenData.iloc[:, 0]
y = messdatenData.iloc[:, 1]

def gerade (x,m,b):
    return m*x+b



plt.figure()
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("y")
plt.show()
