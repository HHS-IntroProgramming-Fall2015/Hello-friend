"""

hellofriend.py
Author: Avery Wallis
Credit: None

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
