import itertools

count = 0
x = 4
y = 3
z = 3
space = {}
z_sum = []
combination_list = []

for i in range(x*y*z):
    #    space["Z{0}".format(n)] = n
    z_sum.append(i)

for n in range(x*y):
    space["Z{0}".format(n)] = []
#   for i in range(3):
#        space["Z{0}".format(n)]

# 6-ot 3-ra módosítottam a számítása gyorsításáért.
for i in itertools.combinations(z_sum, 6):
    count += 1
    combination_list.append(i)
#    filename = 'output.txt'
#    with open(filename, 'a') as f:
#        f.write(str(i))


for z in space.values():
    for i in range(3):
        z.append(z_sum.pop(0))


# for i in itertools.combinations(space.values(), 2):
#    print(i)


print(space)
print(z_sum)
print(count)
print(len(combination_list))


"""
A 4x3x3-as tér indexezése:

Felülnézet:

    |2  5  8  11     |14 17 20 23     |26 29 32 35
   z|1  4  7  10    z|13 16 19 22    z|25 28 31 34
    |0  3  6  9      |12 15 18 21     |24 27 30 33
         x                 x                x
       0.szint          1.szint          2.szint
"""
"""
Kettő kockának a földön kell lennie, és nem lehetnek egymással 
megegyező (eltolt) struktúrák. Ezért egy kockának mindenképp az origóban
kell lennie, egynek pedig az 1, 3, 4 indexek valamelyikén. Mivel rendezett
a lista ezért ez az első két index lesz.
"""
n = 0
for item in combination_list:
    if item[0] != 0:
        del combination_list[n]
    elif item[1] != 1 or item[1] != 3 or item[1] != 4:
        del combination_list[n]
    else:
        n += 1
# Akkor növelem n-t ha nincs törlés, különben kifut az index
print(n)
print(len(combination_list))
"""
Minden kockának érintkeznie kell. Ezért +/-1 vagy +/-3 vagy +/-12 pozícióban
szomszédos párnak kell lennie. Ez lehet az index listán belül bárhol.
"""
n = 0
for item in combination_list:
    for first in range(6):
        for second in range(6):
            if item[first] == item[second]:
                pass
            elif item[first]-1 != item[second] and item[first]+1 != item[second]:
                del combination_list[n]
            elif item[first]-3 != item[second] and item[first]+3 != item[second]:
                del combination_list[n]
            elif item[first]-12 != item[second] and item[first]+12 != item[second]:
                del combination_list[n]
            else:
                n += 1
# Akkor növelem n-t ha nincs törlés, különben kifut az index
"""
Maximum 1 erkély (1 kocka aminek nincs alátámasztása):
Max 1 olyan eset ahol van olyan x>11 aminek nincs 
"""

print(n)
print(len(combination_list))
# print(combination_list)
