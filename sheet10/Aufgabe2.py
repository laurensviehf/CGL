import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- Teil A: Symbolische Berechnung ---
t, A, gamma, omega = sp.symbols('t A gamma omega')
dA, dgamma, domega = sp.symbols('dA dgamma domega')

x_expr = A * sp.exp(-gamma * t) * sp.cos(omega * t)

dx_dA = sp.diff(x_expr, A)
dx_dgamma = sp.diff(x_expr, gamma)
dx_domega = sp.diff(x_expr, omega)

delta_x_expr = dA * sp.Abs(dx_dA) + dgamma * sp.Abs(dx_dgamma) + domega * sp.Abs(dx_domega)

func_x = sp.lambdify((t, A, gamma, omega), x_expr, 'numpy')
func_delta_x = sp.lambdify((t, A, gamma, omega, dA, dgamma, domega), delta_x_expr, 'numpy')

# --- Teil B: Numerische Simulation & Plot ---
t_vals = np.linspace(0, 20, 400)

def create_plot(params, title):
    A_v, dA_v, g_v, dg_v, w_v, dw_v = params
    x_vals = func_x(t_vals, A_v, g_v, w_v)
    dx_vals = func_delta_x(t_vals, A_v, g_v, w_v, dA_v, dg_v, dw_v)
    
    plt.figure(figsize=(10, 5))
    plt.plot(t_vals, x_vals, 'b-', label='$x(t)$')

    plt.fill_between(t_vals, x_vals - dx_vals, x_vals + dx_vals, color='gray', alpha=0.3, label='Unsicherheit')
    
    plt.title(title)
    plt.xlabel('Zeit t')
    plt.ylabel('Auslenkung x')
    plt.legend()
    plt.grid(True)
    plt.show()

# Erster Plot: Unsicherheit in der Amplitude
create_plot((10, 1.0, 0.1, 0.0, 2.0, 0.0), "Fehlerfortpflanzung: Unsicherheit in A")

# Zweiter Plot: Unsicherheit in der Kreisfrequenz
create_plot((10, 0.0, 0.1, 0.0, 2.0, 0.2), "Fehlerfortpflanzung: Unsicherheit in omega")