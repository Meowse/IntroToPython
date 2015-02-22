def print_first_n(n):
        squig = "%i"
        comma = ","
        tupll = ()
        out = [",".join(squig*n), "%", tuple(range(1, (n+3)))]
        return out

def print_first_nn(n):
    return ("the first " + str(n) +
    " numbers are: " + ", ".join([str(i + 1) for i in range(n)]))


