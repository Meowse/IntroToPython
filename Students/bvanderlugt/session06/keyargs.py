def string3(*args, **kwargs):
    '''
    take any num of strings and print
    out any that are longer than three characters
    '''
    print "the args are : " + str(args)
    print "the kwargs are :" + str(kwargs)
    count = 0
    for i in args:
        if len(i) > 3:
            count += 1
    return count

def stringi(*args):
    '''
    print if the lenght of word is longer than its
    index 
    '''
    count = 0
    for i in args:
        if len(i) > args.index(i):
            count += 1
    return count

# you can unpack lists for args with
# stringi(*["", "h", "bigcat", "littlecat"])

def keyLab(fore_color = "black", back_color = "white", \
           link_color = "blue", visited_color = "purple"):
    print fore_color + " " + back_color + " " + link_color + " " + visited_color
    print "the catch all: " *args


def keykwergs(fore_color = "black", back_color = "white", \
           link_color = "blue", visited_color = "purple"):
    print {"fore_color": fore_color, "
