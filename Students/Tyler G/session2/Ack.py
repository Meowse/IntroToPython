import sys

def Ack(m, n):
    """
    This is the Ackerman function
    which is recursive and I don't understand
    all that well. It returns a non-negative integer.
    """
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ack(m-1,1)
    elif m > 0 and n > 0:
        return Ack(m-1,Ack(m,n-1))

def main():
    m_entry = int((sys.argv[1]))
    n_entry = int((sys.argv[2]))
      
    print Ack(m_entry, n_entry)  

if __name__ == "__main__":
    main()

