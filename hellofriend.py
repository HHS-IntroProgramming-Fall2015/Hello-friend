"""
hellofriend.py
Author: Avery Wallis
Credit: None

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

a = input('Please tell me your name: ')
b = input('Please tell me your age: ')
b = int(b)
d = (25-b)
e = "Hello, "
f = ". Python is "
g = " years older than you are!"
h = " years younger than you are!"
i = "as old as you are!"

if d > 0:
    print(e + a + f + str(d) + g)
    
if d < 0:
    d = abs(d)
    print(e + a + f + str(d) + h)
    
if d == 0:
    print(e + a + f + i)
