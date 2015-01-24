**Questions**

+   membership does not work for sub-sequences of other types (can you think of why?):
A: check this out [1, 2] in [[1, 2], 3, 4] == True
that list is in the other list

+ mutable lists: why did both altered and origninal change?
    * A: because they both refer to the same object

Lecture
----

From here out, we are going to cover all of the material in the lecture notes, or try to.

+ why does the index operation throw an error? b/c it is obvious when slice is out of range, you get an empty list. indexing would throw nulls even if you are in range.

'!' is pronounced 'bang'

**Memorize your buil-in's**
ttps://docs.python.org/2/library/functions.html

+ inline code is usually more efficient, but you should create a line for each var in a functioin **if its name gives meaning to what it does**

assingment is blowing my mind

thing = otherthing # these point at the same object now

Here is how to do a copy otherthing = thing[:]
* note: don't do otherthing = list(thing)*
* You can accidently convert a tuple to a list*

**extra note: note

+ Mutable types should be memorized

*A way to think about object assignment:* any object that points to a value is a handle to carry that value for the time being


---

** HW Notes **

why does:

s = "a really cool string"
p = list(s) # convert s to list
p = [s] # using the literal does not convert to string, which
        # makes sense (should be element [1] of list), BUT!
n = range(10)
n.extend(s) # documentation of .extend says: 
            #  *same as s[len(s):len(s)] = x*
            # extend converts x to a list?

interable != sequence (?) 
# ex. iterable(string) = True # sequence(string) = True
from think python: A string is a sequence of characters. You can access the characters one at a time with the
bracket operator:
sequence === iterable (?) I think this is right

*Errors-- Syntax Error: EOL while scanning string*
On this one I missed a qoutation mark on the string

