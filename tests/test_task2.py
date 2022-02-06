from calculator import root_polynomial, discriminant


def test_discriminant_simple():
    """Tests that the discriminant is correctly calculated
    for simple polynomials f(x) = a*x**2
    """
    a = 1
    b = 0
    c = 0
    expected_discriminant = b**2 - 4*a*c
    assert discriminant(a, b, c) == expected_discriminant


def test_discriminant_non_null_b():
    """Tests that the discriminant is correctly calculated
    for polynomials f(x) = a*x**2 + b*x
    """
    a = 1
    b = 2
    c = 0
    expected_discriminant = b**2 - 4*a*c
    assert discriminant(a, b, c) == expected_discriminant


def test_discriminant_full():
    """Tests that the discriminant is correctly calculated
    for polynomials f(x) = a*x**2 + b*x + c
    """
    a = 2
    b = 3
    c = 4
    expected_discriminant = b**2 - 4*a*c
    assert discriminant(a, b, c) == expected_discriminant


def test_root_polynomial():
    """Tests that the roots are computed correctly
    """
    assert root_polynomial(1, 0, 0) == 0
    assert root_polynomial(4, 4, 1) == -4/8
    assert root_polynomial(1, 1, 1) is None
    assert root_polynomial(1, 0, -1) == (-1, 1)
    assert root_polynomial(2, 3, -2) == (-2, 0.5)
