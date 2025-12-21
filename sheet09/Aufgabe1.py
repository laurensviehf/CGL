import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import scipy as sp

messdatenDataPath = r"sheet09\data.txt"

messdatenData = pd.read_csv(messdatenDataPath, delimiter=',', decimal='.', dtype=float)

x = messdatenData.iloc[:, 0].to_numpy()
y = messdatenData.iloc[:, 1].to_numpy()

def gerade (x,m,b):
    return m*x+b

fitParam, _= sp.optimize.curve_fit(gerade, x, y)
m, b = fitParam

plt.figure()
plt.plot(x, gerade(x, m, b), label=f"Fit: y={m:.2f}x + {b:.2f}", label = "Fitgerade")
plt.plot(x, y, label="Datenpunkte")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
