"""
hellofriend.py
Author: Curtis Pych
Credit: https://www.codesdope.com/python-readreadread/
https://snakify.org/en/lessons/print_input_numbers/
https://www.techwalla.com/articles/how-to-convert-int-to-string-in-python
https://linuxconfig.org/working-with-number-variables-in-python
https://en.wikibooks.org/wiki/Python_Programming/Basic_Math, 

Assignment: Hello Friend

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

name = input("Please tell me your name: ")
b = input("Please tell me your age: ")
c = int(b)
s = 28-c
print("Hello, " + name + ". Python is " + str(s) + " years older than you are!")