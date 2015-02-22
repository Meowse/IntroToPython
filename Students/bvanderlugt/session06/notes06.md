Notes on session 06
---

Questions from the readings:

-Whats up with the '*' and '**' syntax in the function arguements?


map
---
- map() in python is equivalent to apply in R! hazah! relevent programming knowldege from R.

positional arguements are those not pre-defined. Keyword arguements have a default value.

you can apply multiple maps, that is nest them.

- map kind of works like zip if you function takes more than one arg. 

- here is a good excersise to determine the difference between a built in method and a method 'of' a type.

1. str.upper
2. "".upper
3. map("".upper, somelist)
4. map(str.upper, somelist)

Notice that the built in method/function "".upper converts the parens to uppers, but is not a function that will take an arguement (no parens to place args into). str.upper is a function that takes an arg in parens and thus works on iterable lists.

List comprehension
---
lists comprehension cares about the order of the arguements:
[output iterator test]
[x for x in list if condition]


Lambda
---
-lambda goes in list? WHy?

- A quick google search reveals that reduce, filter, map, and even lambda are shunned by Guido  

**lambda lab**
Why does :
 def punch(n):
    lambda_out = [lambda n: n + 1]
    for i in range(n):
        lambda_out.append(lambda_out[(i)]) #returns error: int not callable
        print(lambda_out[i](i))
    return lambda_out()

I am not using i to call anything or mutliply, I am using i to supply and arguement to the lambda at index i???
        
Lecture
---

-Functions are simply names you give chunks of code so that you can use
them repeatedly.

-Functions in Python are 1st class objects. 

- the *pass* method is a do_nothing control flow thing.

**keywords**

