
import csv

# def proba1():
#     item = [0, 5, 9, 13, 14, 16]

#     if item[0] != 0 and (item[1] != 1 or item[1] != 3 or item[1] != 4):
#         print('nope')
#     else:
#         print("yepp")


# def proba2(n):
#     mem = [1]
#     if n == 1:
#         return mem
#     else:
#         for num in range(n-1):
#             add = mem[num] * 6 * (num+1)
#             mem.append(add)
#     return mem


# # print(proba2(6))


# def proba3(n):
#     mem = [1]
#     if n == 1:
#         return mem
#     else:
#         for num in range(n-1):
#             add = mem[num] * (4*(num+1)+1)
#             mem.append(add)
#     return mem


# # print(proba3(6))

# def proba4(x, y, z, n, count=0, result={}, struct={}):

#     #cube = [x, y, z]
#     #struct = {}
#     #result["Struct{0}".format(n)] = struct
#     #struct["C{0}".format(n)] = cube

#     # struct.append(cube)
#     #struct["Cube{0}".format(n)] = []
#     n += 1
#     if n <= 6:
#         for num in range(n):
#             count += proba4(x+1, y, z, n, count, result, struct)
#             count += proba4(x-1, y, z, n, count, result, struct)
#             count += proba4(x, y+1, z, n, count, result, struct)
#             count += proba4(x, y-1, z, n, count, result, struct)
#             count += proba4(x, y, z+1, n, count, result, struct)
#             count += proba4(x, y, z-1, n, count, result, struct)
#         #result["Struct{0}".format(n)] = struct
#         # print(struct)
#     else:
#         count += 1
#         print(count)
#         # result.append(struct)
#         #result["Struct{0}".format(n)] = struct
#         #struct["Cube{0}".format(n)] = [cube]
#         # print(result)
#         # print(len(struct))
#         # return result
#         #result["Struct{0}".format(n)] = struct
#     return count


# #print(proba4(0, 0, 0, 0, 0))
# #proba4(0, 0, 0, 0)


# def proba5(x, y, n=0):
#     if x >= 6:
#         return 1
#     elif y >= 6:
#         return 1
#     else:
#         n += proba5(x+1, y, n)
#         n += proba5(x, y+1, n)
#     n += 0
#     return n

# #
# #print(proba5(0, 0))


# def proba6(n):
#     origo = [0, 0, 0]
#     strukt = [origo]

#     for elem in strukt:
#         strukt["C{0}".format(n)] = cube
#         strukt.append([origo[0]+1, origo[1], origo[2]])
#         strukt.append([origo[0]-1, origo[1], origo[2]])
#         strukt.append([origo[0], origo[1]+1, origo[2]])
#         strukt.append([origo[0], origo[1]-1, origo[2]])
#         strukt.append([origo[0], origo[1], origo[2]+1])
#         strukt.append([origo[0], origo[1], origo[2]-1])


# header = ['name', 'area', 'country_code2', 'country_code3']
# data = [
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA'],
#     ['American Samoa', 199, 'AS', 'ASM'],
#     ['Andorra', 468, 'AD', 'AND'],
#     ['Angola', 1246700, 'AO', 'AGO']
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)


array = [[0, 0, 0], [1, 1, 1]]

# with open('D:/Coding/Python/AI/sandbox.py/result.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(array)


with open('array.txt', 'w') as f:
    f.write(str(array))
