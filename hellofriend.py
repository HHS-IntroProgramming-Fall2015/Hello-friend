"""
hellofriend.py
Author: James Eiler
Credit: N/A

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
Name=input('Please tell me your name: ')
Age=int(input('Please tell me your age: '))
YearsOlderThanYou=((2019-Age)-1991)
print('Hello, {0}. Python is'. format(Name), YearsOlderThanYou ,'years older than you are!')
