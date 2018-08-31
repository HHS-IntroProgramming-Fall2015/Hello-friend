a = input("Please tell me your name: ")

b = input("Please tell me your age: ")

if int(b)<= 27 
print("Hello," + a)
s = "Python is {0} years older than you!"
print(s.format(27-int(b)))

else 
print("Hello," + a)
s = "You are {0} older than python! "
print(s.format(int(b))-27)
