import tkinter as tk
#TypeCasting
x = str("Hello World")
y = int(34)
z = float(34.8)
print(x)
print(y)
print(z)
#Type Method
m = "Hello"
n = 95
print(type(m))
print(type(n))
#Global Variables
h = "Hello Guys"
def my_func():
    h = "Hello Ladies"

my_func()
print("The Greetings Is " + h)
#Global Keyword
k = "Hello"
def My_key():
    global k
    k = "Wazzup"
My_key()
print("The Greet Need To Be One Time Is " + k)