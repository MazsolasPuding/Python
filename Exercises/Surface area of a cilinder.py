from math import pi
import random
a = random.randrange(0, 20)
r = random.randrange(0, 10)
print("a = " + str(a) + "\nr = " + str(r))
area = (2 * r**2 * pi) + (a * 2 * pi * r)
print("Henger felülete: " + str(area))