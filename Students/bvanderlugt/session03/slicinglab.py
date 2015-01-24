sample = "aaabbbccc"


def firstLast(x):
    return x[:1] + x[-2:]


def evOther(x):
    return x[::2]


def missing(x):
    return x[3:-4:2]


def reverse(x):
    return x[::-1]
    

def middle(x):
    thirds = len(x)/3
    first = x[:thirds]
    mid = x[thirds:2*thirds]
    last = x[2*thirds:]
    return last + mid + first