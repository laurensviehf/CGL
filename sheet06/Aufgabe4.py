def get_summation_sq(number):
    """Summiere Quardatzahlen bis N.
    Parameters
    ----------
    number: int
    maximale Zahl N.
    Returns
    -------
    result: int
    aufsummierte Quadratzahlen bis N.
    """
    assert isinstance(number, int) and number >= 1, "Die gegebene Zahl ist keine positive,\
    natürliche Zahl."
    result = 0
    i = 1
    while i <= number:
        result = result + i**2
        i = i+1

    return result
assert get_summation_sq(3) == 14

print(get_summation_sq(5))

