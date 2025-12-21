import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def schwingung (t, A, lambda_, omega):
    return A * sp.exp(-lambda_ * t) * sp.cos(omega * t) 


t = sp.symbols("t", real = True)
A = sp.symbols("A")
lambda_ = sp.symbols("lambda", positive=True, real=True)
omega = sp.symbols("omega", positive=True, real=True)


f_abl = sp.diff(schwingung(t, A, lambda_, omega), t)
f_int = sp.integrate(schwingung(t, A, lambda_, omega), t)
f_lim = sp.limit(schwingung(t, A, lambda_, omega), t, sp.oo)

print("Ableitung:" , f_abl)
print("Integral:" , f_int) 
print("Limes für t gegen unendlich:" , f_lim)

werte = {A: 2, lambda_: 0.5, omega: 3}

f_numerisch = sp.lambdify(t, schwingung(t, A, lambda_, omega).subs(werte), 'numpy')
f_abl_numerisch = sp.lambdify(t, f_abl.subs(werte), 'numpy')

t_array = np.linspace(0, 10, 500)
y_f = f_numerisch(t_array)
y_f_abl = f_abl_numerisch(t_array)

plt.figure()
plt.plot(t_array, y_f, label="Schwingung")
plt.plot(t_array, y_f_abl, label="Ableitung der Schwingung")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.legend()
plt.show()