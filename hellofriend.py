"""
hellofriend.py
Author: Mary Feyrer
Credit: Adam Glueck

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
n=input("Please tell me your name: ")
a=input("Please tell me your age: ")
a = int(a)
b = 2016-a
d = b-1991
h = "Hello,"
p = ". Python is "
y = " years older than you are!"
print(h + n + p + d + y)