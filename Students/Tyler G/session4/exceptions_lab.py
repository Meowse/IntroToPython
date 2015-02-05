def safe_input():
    try:
        input = raw_input("Try to escape this: ")
    except EOFError:
        print "That won't work"
        return None
    except KeyboardInterrupt:
        print "You used Ctrl-C or Ctrl-D."
        return None
    else:
        print "Okay that works"
        return input
    

        

if __name__ == "__main__":  
    safe_input()