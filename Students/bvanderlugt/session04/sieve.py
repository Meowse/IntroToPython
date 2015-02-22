#!usr/bin/env python

# For the case when p == 2
# need to iterate through list of multiples so that
# list[i] in multiples > p
def sieve(n):
    primes = range(2, n+1)
    p = 2        
    while p < n:
        for i in range(p, n+1):
            if i*p in primes:
                primes.remove(i*p)
        p += 1
    return primes


if __name__ == '__main__':
    sieve(30)
