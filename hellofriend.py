"""
hellofriend.py
Author: Robbie
Credit: Introuction to Github with Runpython and Introduction to Runpython

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

f=input("Please tell me your name: ")
g=input("Please tell me your age: ")
a=(24-int(g))
print("Hello, " +f +". Python is " +str(a) +" years older than you are!")