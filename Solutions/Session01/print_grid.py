import sys
import time

def allCaller( sleep = False ):

    if sleep:
        time.sleep(1)

    probPart = raw_input("Which part of the problem do you want? (Type 'exit' to exit) ")

    probPart = numValidator(probPart, allCaller)

    if probPart == 1:
        partOne()
        return None

    if probPart == 2:
        partTwo()
        return None

    if probPart == 3:
        partThree()

    if probPart > 3:
        print "The problem didn't have " + str( probPart ) + " parts!"
        allCaller( True )

def numValidator( input, handler ):

    if input == 'exit':
        exiter()

    try:
        input = int( input )

        if isinstance( input, int ):
            return input
    except:
        pass

    try:
        input = int( round( float( input ) ) )

        if isinstance( input, float ):
            return round( input )
    except:
        pass

    print("Sorry dude, needs to be a number. (Type 'exit' to exit.)")
    handler( True )

def continuer():
    time.sleep(0.5)
    continuerVar = raw_input("Would you like to continue? (y/n) ")

    if continuerVar == "y" or continuerVar == "Y":
        allCaller()
    elif continuerVar == "n" or continuerVar == "N":
        exiter()
    else:
        print "Please input either 'y' or 'n'!"
        continuer()

def exiter():
    sys.exit("Thanks for making grids with me.")

def partOne():
    lineOne = "+ - - - - + - - - - +\n"
    lineTwo = "|         |         |\n"

    output = lineOne +  lineTwo *  4 + lineOne + lineTwo * 4 + lineOne

    print output

    continuer()

def partTwo( randomCrud = False ):
    num = raw_input( "How many rows would you like? " )

    num = numValidator( num, partTwo )

    lineOne = "+ - - - - + - - - - +\n"
    lineTwo = "|         |         |\n"

    output = num * ( lineOne + 4* lineTwo ) +lineOne

    print output

    continuer()

def partThree( randomCrud = False ):
    cols = raw_input("How many columns do you want? ")
    cols = numValidator(cols, partThree)

    rows = raw_input("And how many rows? ")
    rows = numValidator(rows, partThree)

    cap = " - - - - +"
    body = "         |"

    output = rows * ( "+" + cols * cap + "\n" + 4 * ( "|" + body * cols + "\n" ) ) + "+" + cols * cap

    print output

    continuer()

allCaller()