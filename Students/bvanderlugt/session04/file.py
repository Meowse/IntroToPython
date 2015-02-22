#!usr/bin/env/python

import os

os.chdir("/home/blair/Documents/Projects/UWPython/IntroToPython/Examples/Session01/")

f = open('students.txt')
student = f.read()

# Pythony way:
with open('students.txt', 'r') as f:
    read_data = f.read()

with open('students.txt', 'r') as f:
    read_data = f.readlines()
