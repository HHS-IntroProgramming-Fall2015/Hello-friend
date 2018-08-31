"""
hellofriend.py
Author: Rachel Matthew
Credit: none

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
n=input('Please tell me your name: ')
a=input('Please tell me your age: ')
y=27-int(a)
if y<0:
    y=str(abs(y))
    print("Hello, {0}. Python is {1} years younger than you are!".format(n,y))
elif y>0:
    y=str(y)
    print("Hello, {0}. Python is {1} years older than you are!".format(n,y))
else:
    print("Hello, {0}. Python is just as old as you are!".format(n)