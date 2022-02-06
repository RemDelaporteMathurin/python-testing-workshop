def add(a, b):
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


def multiply(a: float or list, b: float or list):
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
        return _vector_scaling(a, b)
    elif isinstance(a, (int, float)) and isinstance(b, list):
        return _vector_scaling(b, a)


def _scalar_product(a, b):
    prod = 0
    for xa, xb in zip(a, b):
        prod += xa*xb
    return prod


def _vector_scaling(vector, scaling_factor):
    return [scaling_factor*x for x in vector]
