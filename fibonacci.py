# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 16:16:42 2015

@author: sahluwalia
"""
# Warmup to get my juices going

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return (cigars >= 40 and cigars <= 60)

#
#You and your date are trying to get a table at a restaurant. 
#The parameter "you" is the stylishness of your clothes, 
#in the range 0..10, and "date" is the stylishness of your date's clothes.
# The result getting the table is encoded as an 
# int value with 0=no, 1=maybe, 2=yes. If either of you is 
# very stylish, 8 or more, then the result is 2 (yes). 
# With the exception that if either of you has style of 2 or less, 
# then the result is 0 (no). Otherwise the result is 1 (maybe). 

def date_fashion(you, date):
    if you >= 8 or date >= 8:
        return 2
    elif you <= 2 or date <= 2:
        return 1
    else:
        return 0


import math
x1=4
x2 = 8
y1=9
y2 = 10
dist = ( (x1-x2)**2 + (y1-y2)**2 )
container = math.sqrt(dist)

def fibonacci(n):
    if n <0:
        return 'None'
    elif n==0:
        print 0
    if n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_series(n, n0=0, n1=1):
    if n < 0:
        return 'None'
    if n == 0:
        print n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)

#Write a function FizzBuzzFrodoBilboGandalf(n) which prints out the
#numbers from 1 to n, replacing numbers divisible by 3 with "Fizz", 
#numbers divisible by 5 with "Buzz", numbers divisible by 7 with "Frodo", 
#numbers divisible by 11 with "Bilbo", and numbers divisible by 13 with "Gandalf".  
#Numbers divisible by multiple factors should display 
#"FizzBuzz", "BuzzBilboGandalf", etc.
        

def FizzBuzzFrodoBilboGandalf(n):
    if n %3 == 0:
        return "Fizz"
    if n % 5 ==0:
        return "Buzz"
    if n % 3 == 0 and n % 5 ==0:
        return "FizzBuzz"
    if n % 7 ==0:
        return "Frodo"
    if n % 11 ==0:
        return "Bilbo"
    elif n % 13 ==0:
        return "Gandalf"

for i in range(1,101):
    print FizzBuzzFrodoBilboGandalf(i)
        
FizzBuzzFrodoBilboGandalf(50)
FizzBuzzFrodoBilboGandalf(30)