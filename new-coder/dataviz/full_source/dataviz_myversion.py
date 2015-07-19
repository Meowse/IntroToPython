# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:42:24 2015

@author: sahluwalia
"""
import csv

MY_FILE = "../sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):

    opened_file = open(raw_file)

    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    parsed_data= []    
    
    fields= csv_data.next()    
    
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
       
    opened_file.close()
    
    return parsed_data

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    # Let's see what the data looks like!
    print new_data

    if __name__ == "__main__":
        main()