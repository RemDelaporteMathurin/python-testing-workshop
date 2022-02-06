def multiply(a, b):
    return a*b


def add(a, b):
    return a + b


def divide(a, b):
    if b != 0:
        return a/b
    else:
        raise ValueError("You tried to divide by zero here!")


def substract(a, b):
    return a - b


def scalar_product(va, vb):
    prod = 0
    for xa, xb in zip(va, vb):
        prod += xa*xb
    return prod
