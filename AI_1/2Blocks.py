result = []
origo = [0, 0, 0]
strukt = {}
n = 0
for item in origo:
    plus = origo.copy()
    minus = origo.copy()
    val = origo[n]

    plus[n] = val + 1
    strukt["A{0}+".format(n)] = plus

    minus[n] = val - 1
    strukt["A{0}-".format(n)] = minus
    n += 1

print(strukt)

for item in strukt.values():
    holder = []
    holder.append(origo)
    holder.append(item)
    result.append(holder)

print(result)
