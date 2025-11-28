def is_even(number):
    """Check, if a given number is even.
    Parameters
    ----------
    number: int
    the number to be checked.
    Raises
    ------
    AssertionError: if the input is not 'int' and not positiv.
    Returns
    -------
    bool:
    'True' if the number is even.
    """
    assert isinstance(number, int) and number >= 1, "Die gegebene Zahl ist keine positive,\
    natürliche Zahl."
    return number % 2 == 0
    
assert not is_even(9)
assert is_even(10)

print(f"is_even(9): {is_even(9)}")
print(f"is_even(10): {is_even(10)}")