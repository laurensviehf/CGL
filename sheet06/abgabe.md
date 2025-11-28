# Aufgabe1 Listen

Das vierte Element:

    print(a[3])

Das vorletzte Element:

    print(a[-2])

Das dritte bis drittletzte Element:

    print(a[2:-2])

Jedes zweite Element:

    print(a[3::2])


Ab dem vierten Element:

    print(a[::-3])

Jedes dritte Element in umgekehrter Reihenfolge ab dem vorletzten:

    print(a[-2::-3])

Das siebte entfrnen:

    list.remove(a, 54)

    print(a)

# Aufgabe 2 Datentypen und Ausdrücke

Es gibt einen fehler da an dem Punkt ```... - "3"``` ein ```string()``` von einem ````float()``` abgezogen werden soll was nicht möglich ist. Da diese nicht vom gleichen Datentyp sind bzw. rechenoperationen sind nur mit ```float()``` möglich.


# Aufgabe3 Gerade / Ungerade

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