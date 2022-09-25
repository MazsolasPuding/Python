def cuber(seed):
    result = []
    structer = {}
    count = 0

    for i in range(len(seed)):
        for j in range(len(seed[i])):
            for n in range(3):
                plus = seed[i][j].copy()
                minus = seed[i][j].copy()
                val = seed[i][j][n]
                # print(val)

                plus[n] = val + 1
                structer["A{0}+".format(n)] = plus

                minus[n] = val - 1
                structer["A{0}-".format(n)] = minus

            for item in structer.values():
                holder = []
                for k in range(len(seed[i])):
                    holder.append(seed[i][k])
                holder.append(item)
                result.append(holder)
                count += 1
    # print(structer)
    print(result)
    print(count)
    return result


seed = [[[0, 0, 0]]]
seed_2 = cuber(seed)
seed_3 = cuber(seed_2)
seed_4 = cuber(seed_3)
seed_5 = cuber(seed_4)
full_list = cuber(seed_5)
