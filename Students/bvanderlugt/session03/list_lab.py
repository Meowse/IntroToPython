#!/usr/bin/env python


def fruit_list():
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print "existing fruit basket: " + str(fruit)
    newFruit = str(raw_input("Enter a fruit to add to the basket: "))
    fruit.append(newFruit)    
    print fruit
    fruitIndex = int(raw_input("Enter fruit index: "))
    print fruit[fruitIndex-1]
    fruit = ["Grapefruit"] + fruit
    fruit.insert(0, "kiwi")
    print fruit
    return fruit


for i in fruit_list():
    if i[0] == "P":
        print i

    

def fruit_two():
    fruit = fruit_list()
    print fruit
    del fruit[-1]
    print fruit
    fruitDel = raw_input("Choose fruit to delete: ")
    dubFruit = fruit*2
    print "dub fruit is: "
    print dubFruit
    
    while fruitDel in dubFruit:
        del dubFruit[dubFruit.index(fruitDel)]

    print "after deletion, dub fruit: "
    print dubFruit


def fruit_three():
    fruit = fruit_list()
    likeFruit = ""

    for i in fruit:

        while likeFruit not in ("yes", "no"):
            likeFruit = raw_input("Do you like %s %s" % (i, "?"))
        
        if likeFruit == "no":
            del fruit[fruit.index(i)]     

fruit_three()


