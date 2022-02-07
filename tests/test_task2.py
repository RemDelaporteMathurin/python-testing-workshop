from sympy import root
from calculator import root_polynomial, discriminant


def test_root_polynomial_degree1():
    """Tests that the correct root is found for degree 1
    """
    assert root_polynomial(0, 2, 1) == -1/2
    assert root_polynomial(0, 3.5, 14) == -14/3.5


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


def test_root_polynomial_negative_delta():
    """Tests that the roots are computed correctly
    when the discriminant is negative
    """
    root1, root2 = root_polynomial(1, 0, 1)
    assert root1 == (0, -1)
    assert root2 == (0, 1)

    root1, root2 = root_polynomial(2, 2, 1)
    assert root1 == (-0.5, -0.5)
    assert root2 == (-0.5, 0.5)


def test_root_polynomial_positive_delta():
    """Tests that the roots are computed correctly
    when the discriminant is positive
    """
    root1, root2 = root_polynomial(1, 0, -1)
    assert root1 == -1
    assert root2 == 1

    root1, root2 = root_polynomial(2, 3, -2)
    assert root1 == -2
    assert root2 == 0.5


def test_root_polynomial_delta_zero():
    """Tests that the roots are computed correctly
    when the discriminant is zero
    """
    assert root_polynomial(1, 0, 0) == 0
    assert root_polynomial(4, 4, 1) == -4/8
