# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:55:52 2015

@author: sahluwalia
"""

def sort_dict(d):
#    new_tuple = {(x,y) for x in d for y in d if x is not y}
    new_tuple = sorted(d.items(), key = lambda x: x[1], reverse = True)
    print(new_tuple)

sort_dict({3:1,2:2,1:3})
sort_dict({1:2,2:4,3:6})

def solution(str):
    while len(str):
        return str[::-1]

solution('world') 


list = [1,2,3,4,5,6,7]
[num for num in list if num % 2] #condition at the end
map(lambda num : num*2, list)
lambda_double = lambda num : num*2
[num * 2 for num in list] #function first


def pow(x,y):
    return x**y
#allows you to perform a binary operation on the 1st 2 elements and then the result on the next items     
reduce(pow, list)
reduce(lambda x,y: x*y, range(1,14))
reduce(lambda x,y: x*y, range(1,1100))



def powerof4(n):
    while n > 4:
        if n % 4 == 1 or n == 1:
            return "True, Wrong result for " + str(n) 
        elif n is not int(n):
            raise TypeError("n can not be an array or a list")
        else:
            break#            return "False, wrong result for " + str(n)

powerof4(16)

        
import math

def powerof4(n):
    try:
        if type(n) == int or type(n) == float:
            return math.log(n, 4).is_integer()
        return False
    except:
        return False

import       
def power_of_two(x):
    while x > 0:
        try:
            if type(n) = int or type(n) == float:
                if x % 2 == 1 or 