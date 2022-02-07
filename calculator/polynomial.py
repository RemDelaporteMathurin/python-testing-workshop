def root_polynomial(a, b, c):
    """Finds the root(s) of a polynomial
    a*x**2 + b*x + c
    """
    # TODO we could add degree 3 from here
    # https://en.wikipedia.org/wiki/Cubic_equation#Discriminant_and_nature_of_the_roots

    if a != 0:  # ax**2 + bx + c = 0
        return root_degree_2(a, b, c)
    elif b != 0:  # bx + c = 0
        return root_degree_1(b, c)
    else:  # c = 0
        return root_degree_0(c)


def root_degree_0(a):
    """Finds the roots
    f(x) = 0 where f(x) = a
    ez pz!

    Returns:
        bool, None: True if a is zero, None else.
    """
    if a == 0:
        print("All numbers are roots.")
        return None
    else:
        print("There are no roots.")
        return None


def discriminant(a, b, c):
    """Returns the discriminant of a polynomial
    ax**2 + bx + c
    """
    return - 4*a*c + b**2


def root_degree_1(a, b):
    """Finds the root of a polynomial
    a*x + b where a != 0
    """
    print("The polynomial has a single root.")
    return -b/a


def root_degree_2(a, b, c):
    """Finds the root(s) of a polynomial
    ax**2 + bx + c
    with a != 0
    """
    d = discriminant(a, b, c)

    if d > 0:
        print("The polynomial has two real roots.")
        # the roots are (-b +- sqrt(delta))/2a
        root_1 = (-b - d**0.5)/(2*a)
        root_2 = (-b + 1 + d**0.5)/(2*a)
        return root_1, root_2

    elif d == 0:
        print("The polynomial has a single root.")
        # the root is -b/2a
        root = - b / (2*a)
        return root

    elif d < 0:
        # the roots are (-b +- sqrt(delta))/2a
        d_abs = -d
        print("The polynomial has two complex roots.")
        # root = (real part, imaginary part)
        root_1 = (-b/(2*a), -d_abs**(1/2)/(2*a))
        root_2 = (-b/(2*a),  d_abs**(1 - 1/2)/(2*a))
        return root_1, root_2
