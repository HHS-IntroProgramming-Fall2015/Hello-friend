"""
hellofriend.py
Author: Ryan Kynor
Credit: 
http://stackoverflow.com/questions/19664840/typeerror-cant-convert-float-object-to-str-implicitly
Milo
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

name = input("Please tell me your name:")
age = input("Please tell me your age:")
int(age)-24
x=(int(age))
y=25-x
print("Hello,") print(name) print(". Python is ") print(age) print(" years older than your are!")
print(y)
print("years older than you.")
#s1 = "You are {0} years old."
#s2 = "pythin is {y} years older than you."
#print(int) s1.format((age))
#print(s2.format(age + 5))