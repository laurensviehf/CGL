import numpy as np

def sieb_des_eratosthenes(N):
    ist_prim = np.ones(N + 1, dtype=bool)
    ist_prim[0] = ist_prim[1] = False

    for p in range(2, int(N**0.5) + 1):
        if ist_prim[p]:

            ist_prim[p*p : N+1 : p] = False
            
    primzahlen = np.nonzero(ist_prim)[0]
    
    return primzahlen

N_test = 50
ergebnis = sieb_des_eratosthenes(N_test)
print(f"Primzahlen bis {N_test}: {ergebnis}")