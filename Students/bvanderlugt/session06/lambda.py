def punch(n):
    lambda_out = [lambda n: n + 1]
    for i in range(n):
        lambda_out.append(lambda_out[i])
    return lambda_out

# here is how you want to call it to see the number output
# my_list = punch(n)
# notice that we get a list out...we could even build another function
# to print the value of each element at position n
        
