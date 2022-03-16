# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:42:06 2022

@author: Viviana
"""

#Pico&Placa
"""
The inputs should be:
    a license plate number (the full number, not the last digit),
    a date (as a String),
    and a time. 
The program should return whether or not that car can be on the road.

Details:
 weekday   plate    day
    M   -   1,2   -  0
    T   -   3,4   -  1
    W   -   5,6   -  2
    Th  -   7,8   -  3
    F   -   9,0   -  4

Hours: 7:00am - 9:30am / 16:00pm - 19:30pm
"""

from datetime import date
car = 0

# Compare day with allowed license plate
def weekday(w, lp):
    pp = [[1,2], [3,4], [5,6], [7,8], [9,0]]    # License plate not allowed in each day
    if w > 4:   # Weekend
        return 'allowed'
    elif lp in pp[w]: # Compares
        return 'go'
    else:
        return 'allowed' 

# main
while True:
    l_plate = input('Enter your license plate number in four digits: ')
    if len(l_plate) == 4:       # Compares number of digits
        if l_plate.isdigit():   # Compares if the license plate is a number
            x = int(l_plate[3]) # Takes last digit
            while True:
                try:
                    yy, mm, dd = input('Enter a date YYYY/MM/DD: ').split('/')  # Splits data entered to find date
                    y = weekday(date(int(yy),int(mm),int(dd)).weekday(),x)      # Finds weekday from 0 - 6. Monday = 0
                    break
                except ValueError:
                    print('Wrong date! Please, correct')
                    continue
            if y == 'go':
                while True:
                    hh,tm = input('Enter a time HH:MM in 24 hour format: ').split(':')  # Splits data entered to have time
                    hh,tm = int(hh),int(tm) # Transforms string to integer
                    if hh >= 0 and hh <=23 and tm >=0 and tm <=59:  # Determines if time is in range
                        break
                    else:
                        print('Wrong time! Please, correct')
                        continue
                #7:00am - 9:30am / 16:00pm - 19:30pm
                if (hh >= 7 and hh < 9) or (hh >= 16 and hh < 19):  # Inside Pico y Placa
                    car = 1
                elif (hh == 9 or hh == 19) and tm <= 30: # Last half an hour of Pico y Placa
                    car = 1
                else:
                    car = 0
        else:
            print('Please enter numbers only')
            continue
    else:
        continue
    
    # Allow
    if car == 0:
        print('\nYour car is ALLOWED to be on the road')
    else:
        print('\nYour car is NOT ALLOWED to be on the road')
        
    # Start again
    if input('Do you want to enter another license plate number?\nEnter N to stop or any other key to continue: ') == ('n' or 'N'):
        break
    else:
        continue

print('\nBye! Have a nice day :)')