msg = "Hello World"
msg_2 = "Fuck  Off"
szam = 2
szam_2 = 5

if szam_2 > 1:
    print(msg)
if szam == 2:
    print("Please " + msg_2)

def func():
    msg_2 = ", sorry didn't mean that."
    print(msg + msg_2)

func()

def global_var():
    global x
    x = "12"

global_var()
print("X = " + x)

import random
y = random.randrange(1, 50)
print(y)

z = """This is a multiline
        Comment!"""
print(z)
print(z[3])