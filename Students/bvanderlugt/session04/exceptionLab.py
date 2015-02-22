def safe_input():
    try:
        x = raw_input('enter a string')
        return x
    except (KeyboardInterrupt, EOFError):
        print "Returning None, safely"

