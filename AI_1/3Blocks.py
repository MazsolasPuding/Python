
def cuber(origo):
    result = []
    strukt = {}

    for building in origo:
        for n in range(3):
            plus = origo.copy()
            minus = origo.copy()
            val = origo[n]

            plus[n] = val + 1
            strukt["A{0}+".format(n)] = plus

            minus[n] = val - 1
            strukt["A{0}-".format(n)] = minus

    print(strukt)

    for item in strukt.values():
        holder = []
        holder.append(origo)
        holder.append(item)
        result.append(holder)

    print(result)
    return result


result = cuber([0, 0, 0])
cuber(result)
