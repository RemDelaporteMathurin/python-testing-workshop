def add(a: int or float or list, b: int or float or list):
    # addition of two scalars
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        # addition of two vectors
        return [x1 + x2 for x1, x2 in zip(a, b)]


def divide(a, b):
    if b != 0:
        return a/b
    else:
        raise ValueError("You tried to divide by zero here!")


def multiply(a: int or float or list, b: int or float or list):
    """Multiplies two entities (scalars of vectors)

    Returns:
        list or float: the result of the multiplication
    """
    # multiplication of two scalars
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a*b
    # scalar product of two vectors
    elif isinstance(a, list) and isinstance(b, list):
        return _scalar_product(a, b)
    # mulitplication of a vector by a scalar
    elif isinstance(a, list) and isinstance(b, (int, float)):
        return _scale_vector(a, b)
    elif isinstance(a, (int, float)) and isinstance(b, list):
        return _scale_vector(b, a)


def _scalar_product(a: list, b: list):
    prod = 0
    for xa, xb in zip(a, b):
        prod += xa*xb
    return prod


def _scale_vector(vector: list, scaling_factor: int or float):
    return [scaling_factor*x for x in vector]
