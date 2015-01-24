def fibonacci(n):
    """Return the nth finonacci value."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
