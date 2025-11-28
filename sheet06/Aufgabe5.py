def fak(n):
    """Berechne das Produkt aller natürlichen Zahlen von 1 bis n.
    Parameters
    ----------
    n: int
    Returns
    -------
    result: int
        Produkt aller natürlichen Zahlen von 1 bis n.
    """
    assert isinstance(n, int) and n >= 1, "Die gegebene Zahl ist keine positive, natürliche Zahl."
    
    result = 1  
    i = 1

    while i <= n:
        result = result * i
        i = i + 1  
        
    return result

assert fak(3) == 6 

e_approx = 1.0

k = 1

while k <= 10:
    term = (1**k)/fak(k)
    e_approx = e_approx + term
    k = k+1

print(e_approx)