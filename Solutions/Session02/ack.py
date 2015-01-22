def ackermanFunc(m, n):

    """Take two numbers, m and n and run the Ackerman Function on them."""

    """First validate that they're both positive."""
    if m < 0 or n < 0:
        return None

    """Run the function"""
    if m == 0:
        n+1
    elif m > 0 and n == 0:
        m = m - 1
        ackermanFunc(m, 1)
    else:
        mMin = m - 1
        nMin = n - 1
        newN = ackermanFunc(m, nMin)
        ackermanFunc(mMin, newN)

    return (m, n)

if __name__ == '__main__':

    assert ackermanFunc(0,0) == 1
    assert ackermanFunc(1,1) == 3
    assert ackermanFunc(2,2) == 7
    assert ackermanFunc(3,3) == 61
    assert ackermanFunc(4,4) == 125

    assert ackermanFunc(-1, 0) == None
    assert ackermanFunc(2, -1) == None

    print "All Tests Pass"