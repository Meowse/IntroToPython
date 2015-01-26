def fibonacci(n):
    """
    Returns the nth value of the fibonacci sequence.
    """
    sequence = [0,1]
    for i in range(n-2):
        sequence.append(sequence[len(sequence)-2] + sequence[len(sequence)-1])
    return sequence[n-1]

def lucas(n):
    """
    Returns the nth value of the lucas sequence. It is
    the same as the fibonacci series except the starting 
    numbers are 2 and 1 instead of 0 and 1.
    """
    sequence = [2,1]
    for i in range(n-2):
        sequence.append(sequence[len(sequence)-2] + sequence[len(sequence)-1])
    return sequence[n-1]

def sum_series(n, o = 0, p = 1):
    """
    First parameter returns nth value of series. The second 
    and third optional parameters allows the user to define 
    the first two values in the fibonacci sequence.
    """
    sequence = [o, p]
    for i in range(n-2):
        sequence.append(sequence[len(sequence)-2] + sequence[len(sequence)-1])
    return sequence[n-1]

def main():
    n_entry = int((sys.argv[1]))
    o_entry = int((sys.argv[2]))
    p_entry = int((sys.argv[3]))
    
    print sum_series(n_entry, o_entry, p_entry)  

if __name__ == "__main__":
    main()