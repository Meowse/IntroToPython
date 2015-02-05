import os
from collections import Counter

print "The current working directory is: ", os.getcwd()
print "\n"

path = 'C:\mystuff\pythonclass\introtopython\examples\session01'
os.chdir(path)

print "Now the current working directory is: ", os.getcwd()
print "\n"
print "The files in this directory are: ", os.listdir(path)
print "\n"

file = open("students.txt", "r")
lines = file.readlines()

languages = []

for line in lines[1:]:
    for item in line[line.index(':') + 1:].split(', '):
        languages.append(item.strip())

for index, value in enumerate(languages):
    if value == '':
        languages.pop(index)

hash_languages = Counter(languages)

for key, value in hash_languages.iteritems():
    if key == '':
        pass
    else:
        print "%d student(s) know the '%s' language" % (value, key)
 
file.close()