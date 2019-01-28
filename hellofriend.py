"""
hellofriend.py
Author: Carlton
Credit: Github Tutorial

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

name = input("Please input name.")
birthyear = int(input("Please input year of birth."))
releaseyear = 1991

agedif = birthyear - releaseyear
pnagedif = abs(agedif)

if agedif == -1:
    print("Hello, {0}. Python is 1 year younger than you!".format(name))
elif agedif == 1:
    print("Hello, {0}. Python is 1 year older than you!".format(name))
elif agedif == 0:
    print("Hello, {0}. You are the same age as Python!".format(name))
elif agedif < 0:
    print("Hello, {0}. Python is {1} years younger than you!".format(name, pnagedif))
else:
    print("Hello, {0}. Python is {1} years older than you!".format(name, agedif))