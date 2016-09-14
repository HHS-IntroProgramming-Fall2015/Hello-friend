"""
hellofriend.py
Author: Liam
Credit: Wilson

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
friend=input("Please tell me your name: ")
f_age=input("Please tell me your age: ")
p_age=25
diff=int(p_age) - int(f_age)
s1= "Hello{0}. Python is {1} years older than you are!"
print(s1.format(friend,diff))