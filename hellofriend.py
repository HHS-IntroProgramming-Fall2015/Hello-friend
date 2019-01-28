"""
hellofriend.py
Author: sth23
Credit: https://www.w3schools.com/

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

import datetime
current_year = datetime.datetime.now().year
name = input("What is your name?")
user_age = int(input("How old are you?"))
python_age = current_year - 1991
difference = user_age - python_age
if (difference > 0):
    print("Hello, " + name + ". You are " + str(difference) + " years older than Python.")
elif (difference < 0):
    print("Hello, " + name + ". Python is " + str(-difference) + " years older than you.")
elif (difference == 0):
    print("Hello, " + name + ". You and Pythhon are the same age.")

    