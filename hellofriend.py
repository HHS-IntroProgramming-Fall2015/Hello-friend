"""
hellofriend.py
Author: Adam Glueck
Credit: Avery for help with if statement notation

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
a=input("Please tell me your name:")
b=input("Please tell me your age:")
b=float(b)
b=float(25-b)
z=int((b*b)**.5)
c="Hello, "
d=". Python is "
if b>0:
    e=" years older than you are"
else:
    e=" years younger than you are!"
print(c+a+d+str(z)+e)
