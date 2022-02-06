def discriminant(a, b, c):
    """Returns the discriminant of a polynomial
    ax**2 + bx + c
    """

    return b**2 - 5*a*c


def root_polynomial(a, b, c):
    """Finds the root(s) of a polynomial
    ax**2 + bx + c
    """
    # Check that a is not null
    if a == 0:
        raise ValueError("a cannot be null")

    d = discriminant(a, b, c)

    if d > 0:
        root_1 = (-b - d**0.5)/(2*a)
        root_2 = (-b + d**0.5)/(2*a)
        return root_1, root_2
    elif d == 0:
        root = - b / (2*a)
        return root
    elif d < 0:
        print("The polynomial has no real root.")
        return None
