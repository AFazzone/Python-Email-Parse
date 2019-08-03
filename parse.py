# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:06:11 2019

@author: alf11
"""

import csv 

infile = open("email.txt", "r")
email = infile.read()

mail_list = email.split("\n")
#Splits email into lines


excel_list = []
for line in mail_list:  #For each line in the email
    colon = line.index(":")
    #Finds the colon on the line
    string = "".join(line[colon+1:])
    #only keeps info to the right of the colon
    new_string = string.strip()
    excel_list.append(new_string)
    #makes a new list of important data
    
    
print (excel_list)
location = str(excel_list[12])
city, state, zipcode = location.split(" ")
#separates the name state and zip from 

name = str(excel_list[1])
first, last = name.split(" ")
#separates first and last name

phone = str(excel_list[4])
county = str(excel_list[9])    
street = str(excel_list[10]) 

comment1 = str(excel_list[17]) 
comment2 = str(excel_list[18]) 
comment3 = str(excel_list[19]) 
comment4 = str(excel_list[20]) 
status = ""

schedule_list = [status, first, last, street, city, state, zipcode, county,
                 phone, comment1, comment2, comment3, comment4]
#ordered list 

with open ('mycsv.csv', 'w', newline = "") as f:
    the_writer = csv.writer(f)
    
    the_writer.writerow(["Status","First", "Last", "Address", "City", "State", "Zip",\
                          "County", "Phone", "Comment1", "Comment2", \
                         "Comment3", "Comment4"])
    #columns
    the_writer.writerow(schedule_list)
    
    
    

    
 
