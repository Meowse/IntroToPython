# Slicing lab
def switch(n):
    return n[-1:] + n[1:-1] + n[:1]

def every_other[n]
    return n[::2]

def big_string(n):
    return every_other(n[4:-4]) 
    
def big_strip2(n):
    return n[4:-4:2]

def reverse_sequence(n):
    return n[::-1]
    
def third_chop(n):
    thirds = len(n) / 3
    first_third = n[:thirds]
    middle_third = n[thirds:2*thirds]
    last_third = n[2*thirds:]
    return middle_third + last_third + first_third
    
    
    
# Session 3 Extra Credit
def FizzBuzzAll(n, dictionary = None):
    if dictionary == None:
        dictionary = {3: "Fizz", 5: "Buzz", 7: "Frodo", 11: "Bilbo", 13: "Gandalf"}
    assert type(n) == int and type(dictionary) == dict, "You must insert an integer and an optional dictionary."
    for num in range(1, n + 1):
        holder = " "
        for value in dictionary:
            if num % value == 0:
                holder += dictionary[value]
        if holder != " ":
            print holder.lstrip(" ")
        else:
            print num
         
