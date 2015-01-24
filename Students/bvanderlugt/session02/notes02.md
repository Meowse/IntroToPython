Intro to Python 02
1/15/2015

Note: Github is not letting me push files w/o password. 
Da hell is going on with my ssh?

**Q from HW:** validating raw_input()

pass: tells python there is an empty block. similar to: 
function() {   
}
Nothing betwee the mustaches, in python we dont have curly whirly
bars so we use pass!

things that make code non-reusable: calling sys.exit(), this command
breaks out of the interpreter 

switch is actuallly pretty tricky, so it maybe is a good idea to 
drop it from Python. Switch statements have 'fallthrough' and will
return multiple cases, hence the need for a break. In C, 'bless its
heart', there break is not manditory and fallthrough has lead to tons
of bugs, in C#, break is mandatory and is just noise. Not compelling
reasons for switch.

+ "Premature optimization is the root of all evil." - Donald Knuth

+ "There are two ways to make a software design: so simple that there are obviously no deficiencies, and so complex that there are no obvious deficiencies." - C. A. R. Hoare

+ "O(n^2) is too slow.  Less than O(n^2) is fast enough." - Mickey Phoenix

Tuples are immutable, lists are mutable

Tuple is made with '()', list is made with '[]'

**idomatic python** tuples are more idiomatic when you do not want
your user to change something, you *can* use a list, but a tuple
explains your intention clearer.

**bad error messages** are a window into the working of Python.
Use errors to learn about Python.

ex. 'int' object is not iterable

**idiomatic python** swap in python foo, bar == bar, foo

play with this for a bit:

bob = (4,)
bob = (4,2)
bob , ted = ()
bob = ()

Mickey's fizzbuzz:

    # bad because less readable
    # if not n % 3:
    # evals to 0 == False

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n

for i in range(1,101):
    print fizz_buzz(i)

*note* on return in iPython, the Out syntax for ipython shows side
effects from functions 

**Compare to my fizz_buzz**

def fizz_buzz():
    for i in range(1, 101): # my loop is inside of function
        if i % 3 == 0:
            print "Fizz" # I used print in function, but Mickey said
                         # print is hard to debug  
        if i % 5 == 0:
            print "Buzz"
        else:            # Mickey used the behavoir of return to 
                         # to go through conditions, rather than
                         # call else, he ran return on the last 
                         # condition
            print(i)

I really like specifying the function outside of the for each loop.
using return in the funciton call, and print in the for loop.
I like how the return breaks the function, so there is no need for 
else.

