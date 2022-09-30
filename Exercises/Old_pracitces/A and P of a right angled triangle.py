import random
a = random.randrange(1, 10)
b = random.randrange(1, 10)
print("a = " + str(a) +  "\n"  + "b = " + str(b))
import math
c = math.sqrt(a**2 + b**2)
print("c = " + str(c))

P = round((a + b + c), 2)
A = round((a * b / 2), 2)
print("Parameter = " + str(P))
print("Area = " + str(A))