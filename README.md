# "Pico y Placa" predictor
This code determines whether a car is authorized to circulate by comparing the last digit of its license plate with the numbers established by Quito's regulations.

## General information
"Pico y Placa" prohibits cars with certain license plates from circulating at a certain time of the week.

### "Pico y Placa" Details:
Weekday - License Plate Last Digit:
* Monday - 1,2
* Tuesday - 3,4
* Wednesday - 5,6
* Thursday - 7,8
* Friday - 9,0

Hours:
* AM: 7:00 - 9:30 
* PM: 16:00 - 19:30

## Code Specifications
In order to write the code, there were some parameters to be considered.

The inputs should be:
* a license plate number (the full number, not the last digit),
* a date (as a String),
* and a time. 

The program should return whether or not that car can be on the road.

## Language used
This code is created with:
* Python: 3.7
