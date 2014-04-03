#If you want to run the tests then use -v option

def factorial(n):
    '''Return the factorial of the given integer.

    >>> factorial(1)
    1

    >>> factorial(3)
    6

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    Factorials are valid for an positive integers:
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials are valid for an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    Cannot handle very large numbers:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large

    '''

    import math

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()