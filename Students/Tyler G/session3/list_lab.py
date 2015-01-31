fruits = ["Apples", "Pears", "Oranges", "Peaches"]

for fruit in fruits:
    print fruit
    
new_fruit = raw_input("What kind of fruit would you like you to add to the list? ")
fruits.append(new_fruit)

for fruit in fruits:
    print fruit

number = raw_input("Enter a whole number: ")
try:
    number = int(number)
except ValueError:
    print "Must be a whole number!"

x = 0
for i in range(number,number + len(fruits)):
    print "%i is to %s." % (number, fruits[x])
    number += 1
    x += 1

fruits.insert(0,"Bananas")

print "Only fruits which start with 'p':"
for fruit in fruits:
    if fruit[0].lower() == "p":
        print fruit

print "Full list:"        
for fruit in fruits:
    print fruit
    
fruits.pop(0)

print "First element removed:"
for fruit in fruits:
    print fruit

removed_fruit = str(raw_input("Type the name of the fruit you wish to remove from the list: "))

list_size = len(fruits)
for fruit in fruits:
    if removed_fruit.lower() == fruit.lower():
        fruits.remove(fruit)
if list_size == len(fruits):
    print "Could not find '%s' in the list of fruits!" % removed_fruit

print "Full list:"        
for fruit in fruits:
    print fruit

   
for fruit in fruits:
    print "Do you like %s?" % fruit
    removed_fruits = []
    while True:
        question = raw_input("Enter 'yes' or 'no': ")
        if question.lower() == "no":
            print "Removing %s.." % fruit
            removed_fruits.append(fruit)
            break
        elif question.lower() == "yes":
            print "Keeping %s.." % fruits
            break
        else:
            print "You must enter 'yes' or 'no'!"
for fruit in fruits:
    if fruit in removed_fruits:
        fruits.remove(fruit)    
   
    
print "Here's the list of fruits again: "
for fruit in fruits:
    print fruit
    
new_fruits = []

for i in fruits:
    new_fruits.append(i[::-1])

print "Now here's the fruit list with each element reversed: "
for i in new_fruits:
    print i