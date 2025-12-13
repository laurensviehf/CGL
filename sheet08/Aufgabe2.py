import numpy as np
import matplotlib.pyplot as plt
import argparse

A = 1.0 
gamma = 0.2
omega = 2 * np.pi

t = np.linspace(0, 10, 500)

x = A * np.exp(-gamma * t) * np.cos(omega * t)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label=f'Dämpfung $\gamma={gamma}$')

plt.title('Gedämpfte harmonische Schwingung')
plt.xlabel('Zeit t')
plt.ylabel('Auslenkung x(t)')
plt.legend()
plt.grid(True) 


output_filename = 'damped_oscillation_plot.pdf'
plt.savefig(output_filename)
print(f"Plot gespeichert als {output_filename}")

plt.show()

