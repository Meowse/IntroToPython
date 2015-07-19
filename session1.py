# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 11:42:53 2015

@author: sahluwalia
"""

## Given an int n, return the absolute difference between 
## n and 21, except return double the absolute difference if n is over 21. 


## We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
## We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. 
def parrot_trouble(talking, hour):
    hours = range(24)
    
    for hour in hours:
        if hour >= 7 or hour <= 23:
            talking = "True"
            print talking
        else:
            talking = "False"
            print talking
            
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 

def makes10(a,b):
    sum = a + b
    if sum == 10:
        return True
    if a == 10:
        return True
    elif b == 10:        
        return True
    else:
        return False
  
#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.   

def near_hundred(n):
    if abs(n - 100) <= abs(10):
        return True
    if abs(n - 200) <= abs(10):
        return True
    else:
        return False
        
#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative. 
 
def pos_neg(a, b, negative):
   if "negative":
      return (a > 0 and b > 0)
   else:
      return (a > 0 and b < 0) or (a < 0 and b > 0) 


#Given a string, return a new string where "not " has been added to the front. 
#However, if the string already begins with "not", return the string unchanged. 

def not_string(str):
       
        if len(str) < 3 and str[3:] == "not":        
            return "str"
        else:
            return 'not' +  "str"
            
def string_bits(str):
   return len(str)>1 and str[0:n+1]


def string_splosion(str):
    for i in str:
        return str + str[:i+1] 

def last2(str):
    if len(str) < 2:
        return 0

last2 = str[-2:-1]
count = 0  
return + str[-2:-1]
    for i in range(len(str)-2:
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1
            return count
    
    
def array_count9(nums):
    count = 0
    for n in nums:
        if n == 9:
            count = count + 1
        return count
     
array_ count9
 

