# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 17:23:46 2015

@author: sahluwalia
"""
cohort1 = {
    'Avery': [63, 62, 41, 66, 84, 82, 73, 89, 69, 75],
    'Blake': [79, 97, 78, 78, 74, 69, 80, 100, 74, 70],
    'Casey': [93, 97, 99, 95, 98, 91, 96, 99, 100, 88],
    'Dakota': [71, 65, 72, 65, 24, 100, 84, 71, 59, 50],
    'Elliot': [84, 73, 90, 72, 69, 93, 61, 65, 81, 98],
    'Fox': [80, 91, 90, 80, 83, 73, 84, 89, 84, 84],
    'Gale': [41, 7, 64, 60, 78, 48, 73, 50, 69, 89]
}


#student_means: Return a new dictionary, with students as keys and their mean test score as the value.
#Then add an optional argument, drop_lowest. When true, drop each student's lowest score before calculating their mean.

def scores(long_dictionary):
    class_averages = [(sum(val),len(val), sum(val)/len(val)) for val in long_dictionary.itervalues()]
    name = []
    final = zip(class_averages, name)
    for key in long_dictionary.iterkeys():
        name.append(key)
    #return class_averages
    #return list(name)
    final = zip(class_averages, name)
    final.sort()
    print("This is the final data set: " + str(final))
    
scores(cohort1)

#student_grades: Return a new dictionary, with students as keys and their grade as the value. 
#Add the optional drop_lowest argument like in student_means. A is 90+, B is 80-89, C is 70-79, D is 60-69, F is below 60.


#all_scores: Return a list of all the students' test scores.
#class_mean: Return a float, the mean score for the entire class across all tests.
import operator  
def allscores(scores):
    vals = []
    for val in scores.itervalues():    
        vals.append(val)
    merged = reduce(operator.add, vals)
    sum_means = reduce(lambda x, y: x + y, merged)/len(merged)
    print(sum_means)
    
allscores(cohort1)

#score_histogram: Return a new dictionary. Each key is a letter grade (A, B, C, D, F).
#The value for each is all the students' test scores that fall within that grade range.
def grade_histogram(lst):
    lst_vals = [(lst[v]) for v in lst.itervalues()]  #TypeError: unhashable type: 'list'

    return lst_vals
    for element in lst:
            if element in lst and element in range(90,101):
                print("A")
                lst[element] = 1
            if element in lst and element in range(80,90):
                print("B")
                lst[element] = 1
            if element in lst and element in range(70,80):
                print("C")
                lst[element] = 1
            if element in lst and element in range(60,70):
                print("D")
                lst[element] = 1          
            else:
                lst[element] =  lst[element] + 1
            print(lst)

grade_histogram(cohort1)
 
