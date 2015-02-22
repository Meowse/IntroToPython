Sessoin 04
----

breaks and ___ are generally a sign of messy code. 

enumerate(some_tuple) same as zip(range(len(some_tuple)))

Python-y: for i in iterable-thing
non-Python-y: for i in range(len(some_thing))

In regards to putting together large strings:
Do not use succesive string concatinations, use join.
It is much for efficient because it measures how big of a string
you need and fills it. 

note on join: you can't do "".join(1,2,3) because join only works on
strings. You ave to do a list comprehension first

Python-y way to build a list: List comprehension
[str(i + 1) for i in range(n)]
list comprehension means turning each element in a list into its
own string. Most naive methods just turn the whole list into a string
a la str([1, 2, 3]) does not work

*I think* list comprehension is nuts because it realies on an inline
for loops, you can define i in range anywhere in the code line and then
call i at any place in the line. its crazy because you don't have to
end the for call in ':'

    for i in something:

*actually* As I think about it, in R you can do inline function calls
and omit the curly braces, so I guess it makes sense... 

    function(x) sum(x)

Pro-tip: when mickey solved the print_first_n() problem he broke it
down into smaller pieces. He started with the list of integers, converting
it into a tuple. Then he 

I need more string and slicing excercises...
1) print out every third element of a list, but square the fifth
2) sieve of erastosthenes

Hash tables are the shit. they trivialize problems.

Anything that is mutable cannot be used as a key in a dict

Every variable is in a dict, its hella optimized 

I still don't really know how enumerate works

.setdefualt() look for a set if its not there create a new set and
put thing there

HW: work on exceptions before class
exception handling semantics are crucial to understand

Notes on Sieve of athstonimicallessss:
---
range does the the closed form of a range: 
2:5 is like 2 through n < 5...so it equals: 2, 3, 4

Lab: Dictionaries and sets

To create the counts of t's I used:
t = somedict.values()
t.count('t')
dict(zip(somedict.keys, t.count('t')))