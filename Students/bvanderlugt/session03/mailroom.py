donors = {'Bob Lawbla': [10, 20, 30], 'Steve Bee': [2], 
'Eric Smutz': [10, 30], 'Linda Hannigan': [30, 5], 
'Katie Shmatie': [1, 3, 9]}

def mailroom():
    response = ""
    while not response.lower() == 'send a thank you' or not response.lower() == 'create a report':
        response = raw_input("Would you like to send a thank you or create a report?")




mailroom()
