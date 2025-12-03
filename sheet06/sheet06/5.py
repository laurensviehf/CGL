def fak(n):
    """Berechne das Produkt aller natürlichen Zahlen von 1 bis n.
    Parameters---------
    n: int
    Returns------
    result: int
    Produkt aller natürlichen Zahlen von 1 bis n.
    """
    assert isinstance(n, int) and n >= 1, "Die gegebene Zahl ist keine positive,\
    natürliche Zahl."
    result = 0
    ... # TODO
    
    return result

assert fak(3) == 6