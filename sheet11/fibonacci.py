import numpy as np
import matplotlib.pyplot as plt

# Part 1
v = np.array([1, 1])
M = np.array([[1, 1], 
              [1, 0]])

ratios = []

for i in range(50):
    v = M @ v  # v_neu = M * v_alt
    # Das Verhältnis a_{n+1} / a_n entspricht v[0] / v[1]
    ratios.append(v[0] / v[1])

plt.plot(ratios, linestyle="none", marker="o")

# --- Teil 2: Eigenwerte und Approximation ---
# Eigenwerte (W) und Eigenvektoren (V) berechnen
eigenvalues, eigenvectors = np.linalg.eig(M)
print(f"Eigenwerte: {eigenvalues}")

# Dominanter Eigenwert (lambda_1 > 1)
lam1 = eigenvalues[0] 
O = eigenvectors
O_inv = np.linalg.inv(O)

ratios_approx = []
for n in range(1, 51):
    # Approximation: M^n = O * diag(lam1^n, 0) * O_inv
    D_n_approx = np.array([[lam1**n, 0], 
                           [0, 0]])
    M_n_approx = O @ D_n_approx @ O_inv
    
    # Berechnung des Vektors durch die approximierte Matrix
    v_approx = M_n_approx @ np.array([1, 1])
    ratios_approx.append(v_approx[0].real / v_approx[1].real)

plt.plot(ratios_approx, "r x", label="Approximation")
plt.axhline(y=(1+np.sqrt(5))/2, color="g", label="Grenzwert (Goldener Schnitt)")
plt.legend()
plt.show()
