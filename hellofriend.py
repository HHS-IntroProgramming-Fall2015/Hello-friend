"""
hellofriend.py
Author: waSclthu11
Credit:  I looked at the schoology tutorials.

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
# I had already writted this code and pasted it into a google doc. It has been pasted back into the runpython.
A = (input("Please tell me your name: "))
B = float(input("Please tell me your age: "))
C = int(B)
D = (28-C)
print("Hello, " + (A) + ". Python is " + str(D) + " older than you are!")

