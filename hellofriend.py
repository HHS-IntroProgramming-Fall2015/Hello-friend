"""
hellofriend.py
Author: <your name here>
Credit: Payton; Payton; Payton some more; and oh wait, more Payton

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
name = input("What is your name?")
age = int(input("How old are you?"))
if(age>25):
    s= "Hello, {0}. Python is {1} years {2} than you are!"  
    print(s.format(name, age-25, "younger"))
    


if(age==25):
    

if(age<25):


