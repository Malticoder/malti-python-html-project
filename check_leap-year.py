#!/bin/bash

# FUndction to Validate Number
def valid_number(number):
     if number >0:
          print("given number is positive");
     else:
          print("given number is negative");
# End of FUndction to Validate Number          
          
# Function to check if number represents a leap yaer
def leap_year(year):
     if (year%400 == 0) or (year%4==0 and year%100!=0):
          print("leapyear");
     else:
          print("not leap year");
# End of Function to check if number represents a leap yaer

## Main code starts here
# Asj the user to enter the number 
year_input = int(input("enter a year to check leap year- "))
valid_number(year_input)
leap_year(year_input)