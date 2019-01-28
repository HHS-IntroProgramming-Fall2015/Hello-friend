"""
hellofriend.py
Author: Macy Curtis
Credit: Ella.

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
a = input("Please tell me your name: ",) 
#b = input("Macy")
b = input("Please tell me your age: ",)
c = 2019-int(b)
d = str(c-1991)
print ("Hello, "+a+". Python is "+d+" years older than you are!")
