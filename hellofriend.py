"""
hellofriend.py
Author: <your name here>
Credit: <list sources used, if any>

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
nam=input("Young one, tell me your name:")
ag=input("Young one, tell me your age:")
byr=2015-int(ag)
pyr=byr-1991
z="Hello young {0}. I am Python, the great and powerful computer language. You can tell that I must be a prestigious language as I am {1} years older than you."
print(z.format(nam,pyr))