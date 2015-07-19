# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 14:58:11 2015

@author: sahluwalia
"""

#!/usr/bin/env python

import csv


def read_file(filename):
    with open('filename', 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter = '|')
        data = []
        for row in reader:
            data.append(row)
    return data

data_set = {}
data_files =['name-address.psv', 'name-bank-email.psv']
    
for filename in data_files:
    contents = read_file(filename)
    data_set[filename] = contents

joined_data = {}

for data_set_name in data_set:
    data_set = data_set[data_set_name]
    for row in data_set:
        key = row['name']
        key = key.strip()
        key = key.lower()
        if key not in joined_data:
            joined_data[key] =row
        else:
            data = joined_data[key]
            data.update(row)
            
for row in joined_data.values():
    row_data = row.values()
    print "\t".join(len(row_data)
    
    