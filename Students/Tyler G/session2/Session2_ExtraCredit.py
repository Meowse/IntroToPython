

#Session 2 Extra Credit  
def FizzBuzzFrodoBilboGandalf(n):
    for i in range(1,n+1):
        holder = " "
        if i % 3 == 0:
            holder += "Fizz"
        if i % 5 == 0:
            holder += "Buzz"
        if i % 7 == 0:
            holder += "Frodo"
        if i % 11 == 0:
            holder += "Bilbo"
        if i % 13 == 0:
            holder += "Gandalf"
        if holder == " ":
            print i
        else:
            print holder.lstrip(" ")


FizzBuzzFrodoBilboGandalf(100)