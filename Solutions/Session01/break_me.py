def aNameError():
    return aSyntaxError()

def aSyntaxError():
    #retn aNameError() + 2
    pass

def aTypeError():
    return "heya" + 2

def anAttributeError():
    myObject = 2
    return myObject.something

#aNameError()
#aSyntaxError()
#aTypeError()
#anAttributeError()