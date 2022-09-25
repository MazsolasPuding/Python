import numpy as np

# theta = np.radians(90)
# c, s = np.cos(theta), np.sin(theta)
# R = np.matrix([[c, -s, 0], [s, c,0], [0,0,1]])
# v = np.matrix( [ 1,  -2, 4] )

# res = np.matmul(v, R).astype(int)
# #res = res.astype(int)
# print(res)
# res = np.array(res)

# print(res.shape)
# res = np.squeeze(res)
# res_shape = res.shape
# print(res)
# print(res_shape)


# x = np.array([[[0], [1], [2]]])

# print(x.shape)
# # (1, 3, 1)

# print(np.squeeze(x))
# # (3,)

# print(x)


# x = [[[1,-2,4],[0,2,3],[-2,0,1],[0,-3,2]]]
# print(x)

# for i in range(len(x)):
#     min_x = 0
#     min_y = 0
#     min_x = x[i][0][0]
#     min_y = x[i][0][1]
#     # Get the minimum of the idexes in X and Y direction
#     for j in range(len(x[i])):
#         if x[i][j][0] < min_x:
#             min_x = x[i][j][0]
#         if x[i][j][1] < min_y:
#             min_y = x[i][j][1]
#         # Offset all the cubes in the X, Y direction by the minimum indexes.
#         # From now on, all of the structures are in the first octant of the
#         # 3D cartesian coordinate system, so all coordinates are positive.
#     print(f"x = {min_x}")
#     print(f"y = {min_y}")
#     for k in range(len(x[i])):
#         cube = x[i][k].copy()
#         cube[0] += abs(min_x)
#         cube[1] += abs(min_y)
#         x[i][k] = cube
#     print(x)
#     x[i].sort(key=lambda row: (row[0], row[1], row[2]))
#     print(x)


# def rotaion_filter(seed):
#     """
#     Rotate each strucure around the Z axis 3 times, and checks if the
#     structures are the same using the transition filter.
#     """
#     result = []
#     rotation = {}
#     for i in range(3):
#         key = f"{(i+1)*90}_degree"
#         rotation[key] = seed.copy()
#         theta = np.radians((i+1)*90)
#         c, s = np.cos(theta), np.sin(theta)
#         R = np.matrix([[c, -s, 0],
#                        [s,  c, 0],
#                        [0,  0, 1]])

#         for j in range(len(rotation[key])): #for all structures
#             for k in range(len(rotation[key][j])): #for all cubes (/vectors)
#                 matrix = np.matmul(rotation[key][j][k], R).astype(int)
#                 array = np.array(matrix)
#                 squeezed = np.squeeze(array).tolist()
#                 rotation[key][j][k] = squeezed

#         # print(len(rotation))
#         # print(rotation.keys())
#         # print(len(rotation[key]))

#         rotation[key] = translation_filter(rotation[key], False)
#         print(len(rotation[key]))

#     for i in range(len(seed)):
#         result.append(seed[i])
       
#     print(len(result))



# def rotaion_filter(seed):
#     """
#     Rotate each strucure around the Z axis 3 times, and checks if the
#     structures are the same using the transition filter.
#     """
#     result = []

#     for i in range(len(seed)):
#         rot = []
#         rot.append(seed[i])
#         match = False

#         for i in range(3):
#             theta = np.radians((i+1)*90)
#             c, s = np.cos(theta), np.sin(theta)
#             R = np.matrix([[c, -s, 0],
#                            [s,  c, 0],
#                            [0,  0, 1]])
#             for j in range(len(seed[i])): #for all cubes (/vectors)
#                 matrix = np.matmul(seed[i][j], R).astype(int)
#                 array = np.array(matrix)
#                 squeezed = np.squeeze(array).tolist()
#                 rot.append(squeezed)
#             print(rot)
#             rot = translation_filter(rot, False)
#         for item in rot:
#             if item in seed:
#                 match = True
#             else:
#                 pass
#         if not match:
#             result.append(seed[i])
            
#     print(len(result))


def cuber(seed):
    """
    Adding one cube to each structure specified in the argument, and
    generate all solutions with some "light" filters applied.
    """
    # Without filters the maximum structure count can be calculated as:
    # a(n) = a(n-1)*6*n
    # a(0) = 1; a(1) = 1*6*1; a(2) = 6*6*2; ... ; a(5) = 31.104*6*5 = 933.120
    result = []
    structer = {}
    count = 0
    # for each cube in a structure, 6 new structures are generated ->
    # (3 dimensions * 2 directions).
    # with 6 cubes this function needs to be called 5 times, each time
    # passing the previous one's result as an argument.

    for i in range(len(seed)):      # select each structure
        for j in range(len(seed[i])):   # select ech cube
            for n in range(3):              # select each coordinate
                plus = seed[i][j].copy()
                minus = seed[i][j].copy()
                val = seed[i][j][n]
                # Generate all possible new cube positions
                # and put them in a dictionary.
                # The Z coordinate can't be more than 2.
                if n == 2 and val+1 > 2:
                    pass  # This way the max height is 3 blocks.
                # Can't be longer than 5 blocks from 6 cubes that aren't in one line.
                # elif val+1 > 4:
                #    pass  # Pre-filtering for: Max 4 blocks in a line rule.
                else:
                    plus[n] = val + 1
                    structer["Cube{0}+".format(n)] = plus

                # The Z coordinate can't be negative.
                if n == 2 and val-1 < 0:
                    pass
                else:
                    minus[n] = val - 1
                    structer["Cube{0}-".format(n)] = minus
            # After the dictionary of the new cubes is made, create all new
            # structers, by adding all the previous cubes from a structure
            # to the new cube.
            for item in structer.values():
                if item in seed[i]:  # If a cube is already in a structure, pass
                    pass
                else:
                    holder = []
                    for k in range(len(seed[i])):
                        holder.append(seed[i][k])
                    holder.append(item)
                    result.append(holder)
                    count += 1
    # print(structer)
    # print(result)
    print(count)
    return result


origin = [[[0, 0, 0]]]

def create(origin, number_of_blocks):
    """Create all posible structures."""
    i = 0
    for i in range(number_of_blocks):
        origin = cuber(origin)
    result = origin


create(5)

# two_cubes = cuber(origin)
# three_cubes = cuber(two_cubes)
# four_cubes = cuber(three_cubes)
# five_cubes = cuber(four_cubes)
# six_cubes = cuber(five_cubes)