"""

hellofriend.py
Author: Avery Wallis
Credit: None

"""

a = input('What is your name?')
b = input('How old are you?')
b = float(b)
d = (25-b)
e = "Hello, "
f = ". I am "
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