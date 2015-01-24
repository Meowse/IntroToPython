def ack(m, n):
    """Returns the ackerman function of two numbers."""
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


if __name__ == '__main__':
    assert ack(0, 0) == 1
    assert ack(0, 1) == 2
    assert ack(0, 2) == 3
    assert ack(0, 4) == 5
    print "All tests pass"    
