"""
hellofriend.py
Author: Jasper Meyer
Credit: worked with Brendan


"""
name=input("Please tell me your name: ")
age=input("Please tell me your age: ")
s= ("Hello, {0}. Python is {1} years older than you are!")
print(s.format(name,(26-(int((age))))))