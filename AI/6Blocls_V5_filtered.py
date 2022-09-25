import csv

"""
Generate all possible structures from 6 Blocks with the following rules.
- Minimum 2 blocks on the ground.                                           OK
- All blocks joined (on surfaces).                                          OK
- Max 1 balcony (overhang). Bridges are allowed ((supported on two sides)?) OK
- Max 3 blocks height.                                                      OK
- Max 4 blocks in a singal straight line.                                   OK
- Only unique structures: No matches allowed by translating (or rotating?)  OK
  the structures. Mirroring structures are allowed and needed.
"""


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
                elif val+1 > 4:
                    pass  # Pre-filtering for: Max 4 blocks in a line rule.
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


def two_on_floor(seed):
    """Filters all structures where at least 2 cube is not on the ground."""
    result = []
    for i in range(len(seed)):
        n = 0
        for j in range(len(seed[i])):
            # If a cube's 3rd coordinate is 0, it is on the ground.
            if seed[i][j][2] == 0:
                n += 1
        # If there's less than two blocks, leave out that structure.
        if n >= 2:
            result.append(seed[i])
    print(len(result))
    # print(result)
    return result


def balcony(seed):
    """Filters all structures where there's more than 1 overhanging cube."""
    result = []
    for i in range(len(seed)):
        n = 0
        for j in range(len(seed[i])):
            # Look for a cube underneath this one (Z coordinate - 1)
            support = seed[i][j].copy()
            support[2] -= 1
            # If the support block's Z coordinate is positive and is not in the
            # structure, there is an overhang.
            if support not in seed[i] and support[2] >= 0:
                n += 1
        # If there's more than one overhang, leave out that structure.
        if n < 2:
            result.append(seed[i])
    print(len(result))
    return result


def translation_filter(seed):
    """
    Offsets all structures into the first octant of the 3D cartesian coordinate
    system (lined up with the X and Y axis), and filters out mathcing struct.'s.
    """
    n = 0
    result = []
    for i in range(len(seed)):
        min_x = 0
        min_y = 0
        min_x = seed[i][0][0]
        min_y = seed[i][0][1]
        # Get the minimum of the idexes in X and Y direction
        for j in range(len(seed[i])):
            if seed[i][j][0] < min_x:
                min_x = seed[i][j][0]
            if seed[i][j][1] < min_y:
                min_y = seed[i][j][1]
            # Offset all the cubes in the X, Y direction by the minimum indexes.
            # From now on, all of the structures are in the first octant of the
            # 3D cartesian coordinate system, so all coordinates are positive.
                # for k in range(len(seed[i])):
            # print(min_x)

        for num in range(len(seed[i])):
            seed[num][0] += abs(min_x)
            seed[num][1] += abs(min_y)
        # If a structure is already in the result, do not include it
        if seed[i] in result:
            pass
        else:
            result.append(seed[i])
    # print(result)
    print(n)
    print(len(result))
    return(result)


# def check(seed):
#     four = "Yes"
#     for i in range(len(seed)):
#         for j in range(len(seed[i])):
#             for k in range(len(seed[i][j])):
#                 if seed[i][j][k] == 5:
#                     print(four)
#                     break
# check(offset_cubes)


def four_in_line(seed):
    """
    Filters out structures where there's more than 4 blocks
    in a single straight line.
    """
    result = []
    for i in range(len(seed)):
        n = 0
        for j in range(len(seed[i])):
            # Only look at the first two coordinates (Z>3 already filtered)
            for k in range(2):
                # All structures have at least one cube where X=0, and one
                # where Y=0. So if there's a cube where either of these coord.'s
                # are 4, we need to check the structure.
                if seed[i][j][k] >= 4:
                    mem = seed[i][j][k] - 4
                    for l in range(len(seed[i])):
                        # If there's a cube in the structure where X-4 (or Y-4)
                        # exists, there's five cubes in a
                        if seed[i][l][k] == mem:
                            n += 1
        if n == 0:
            result.append(seed[i])

    print(len(result))
    return result


# The input has to be the same format as the output: 3D matrix (list).
origin = [[[0, 0, 0]]]
two_cubes = cuber(origin)
three_cubes = cuber(two_cubes)
four_cubes = cuber(three_cubes)
five_cubes = cuber(four_cubes)
six_cubes = cuber(three_cubes)


two_on_floor = two_on_floor(six_cubes)
max_1_balcony = balcony(two_on_floor)
offset_cubes = translation_filter(max_1_balcony)
less_than_four = four_in_line(offset_cubes)

with open('result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(less_than_four)
