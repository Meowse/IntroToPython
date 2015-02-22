# square one
def square():
    segment1 = ("+" + "-" * 4) * 2 + "+"
    segment2 = ("|" + " " * 4) * 2 + "|"
    for i in range(1, 12):
        if i == 1 or i == 6 or i == 11:
            print segment1
        else:
            print segment2


# print_grid
# add some kind of half-ass scaling
def print_grid(n):
    # scale the dashes to n, subtract out the +'s
    segment1 = ("+" + "-" * (n - 3)) * 2 + "+"
    segment2 = ("|" + " " * (n - 3)) * 2 + "|"
    # every five lines print segment one
    for i in range(0, n):
        if i % 5 == 0:
            print segment1
        else:
            print segment2


# n by n
def n_grid(x, y):
    # scale both segment lengths to x
    segment1 = ("+" + "-" * (x - 3)) * 2 + "+"
    segment2 = ("|" + " " * (x - 3)) * 2 + "|"
    # scale i to y
    for i in range(0, y):
        if i % 5 == 0:
            print segment1
        else:
            print segment2