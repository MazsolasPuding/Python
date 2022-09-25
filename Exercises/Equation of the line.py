import random
A = [random.randrange(0, 20), random.randrange(0, 20)]
B = [random.randrange(0, 20), random.randrange(0, 20)]
print("A = " + str(A))
print("B = " + str(B))
AB = [(B[0] - A[0]), (B[1] - A[1])]
print("AB = " + str(AB))
N = [-AB[1], AB[0]]
print("N = " + str(N))
#e = N[0] * (x - A[0]) + N[1] * (y - A[1])
e = str(N[0]) + " * (x - " + str(A[0]) + ")" +  " + " + str(N[1]) + " * (y - " + str(A[1]) + ")"
print("e = " + e)
x = N[0]
y = N[1]
szam = N[0] * A[0] + N[1] * A[1]
e = str(N[0]) + "x + " + str(N[1]) + "Y + " + str(szam)
print("e = " + e)
x = round(((x * -1) / y), 2)
szam = round(((szam * -1) / y), 2)
e = "y = " + str(x) + "x + " +  str(szam)
print(e)