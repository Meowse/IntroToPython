def lotr(n):
    s = "" 
    if n % 3 == 0:
        s += "Fizz"
    if n % 5 == 0:
        s += "Buzz"
    if n % 7 == 0:
        s += "Frodo"
    if n % 11 == 0:
        s += "Bilbo"
    if n % 13 == 0:
        s += "Gandalf"
    if len(s) == 0:
        return n
    return s


for i in range(1, 101):
    print lotr(i)

# sqrt
def sqrootz(x1, x2, y1, y2):
    dist = (x1-x2)**2 + (y1-y2)**2
    return dist



