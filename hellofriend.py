"""
hellofriend.py
Author: Morgan Gardner
Credit: None

Assignment: 

Write and submit an interactive Python program that asks for the user's name and age, 
then prints how much older Python is than the user (based on a simple comparison of 
birth year). Python's first public release occurred in 1991. Something like this:

Please tell me your name: Guido
Please tell me your age: 16
Hello, Guido. Python is 8 years older than you are!

Note that the text: "Guido" and "16" are entered by the user running the program. 
The final line ("Hello...") is generated dynamically when you run the program, based 
on the name and age that the user enters.
"""

name = input('What is your name: ')
age = input('Hi ' + name + '. How old are you? ')

a = (27 - int(age))

if a > 0:
    print('Did you know that you are ' + str(a)+ ' years younger than python?')
    
if a < 0:
    print('Did you know that you are ' +str(a*-1) + ' years older than python?' )
    







