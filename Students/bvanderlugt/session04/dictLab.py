# starting at sets because I just ran everythin interactively up to here
s2 = range(21)

for i in s2:
    if i%2==0:
        s2.remove(i)
    s2 = set(s2)

s3 = range(21)

for i in s3:
    if i%3==0:
        s3.remove(i)
    s3 = set(s3)
    
s4 = range(21)

for i in s4:
    if i%4==0:
        s4.remove(i)
    s4 = set(s4)

# check if every thing in s2 is in s4
s2 < s4
