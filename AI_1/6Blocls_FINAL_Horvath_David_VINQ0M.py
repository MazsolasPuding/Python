# Import libraries
import csv
from time import sleep
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


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
    # print(result)
    print(len(result))
    return result


def translation_filter(seed, filt):
    """
    Offsets all structures into the first octant of the 3D cartesian coordinate
    system (lined up with the X and Y axis). If "filt" = True it filters out mathcing structure's.
    """
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
        for k in range(len(seed[i])):
            cube = seed[i][k].copy()
            cube[0] += abs(min_x)
            cube[1] += abs(min_y)
            seed[i][k] = cube
        # If a structure is already in the result, do not include it.
        # Sort each structure along it's 3 coordinate's before adding them,
        # to avoid duplicates.
        seed[i].sort(key=lambda row: (row[0], row[1], row[2]))
        if seed[i] in result and filt:
            pass
        else:
            result.append(seed[i])
    # print(result)
    # print(len(result))
    return(result)


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
                        # exists, there's five cubes in a single straight line.
                        if seed[i][l][k] == mem and j != k:
                            n += 1
        if n == 0:
            result.append(seed[i])
    print(len(result))
    return result


def check_cube_connection(seed):
    """Filter out those structures where not all cubes are connected."""
    result = []
    for i in range(len(seed)):
        n = 0
        for k in range(len(seed[i])):
            # Add and subtract 1 from each coordinate and check if that cube is
            # in the structure. If it is, there's a connection.
            for l in range(3):
                cube_minus = seed[i][k].copy()
                cube_plus = seed[i][k].copy()
                cube_minus[l] -= 1
                cube_plus[l] += 1
                if cube_plus in seed[i] or cube_minus in seed[i]:
                    # If connection add 1 to n.
                    n += 1
        # With 6 cubes, at least 6 connection is needed
        if n <= 6:
            pass
        else:
            result.append(seed[i])
    print(len(result))
    return result


def rotaion_filter(seed):
    """
    Rotate each strucure around the Z axis 3 times, and checks if the
    structures are the same using the transition filter.
    """
    result = []
    # Select each structure
    for i in range(len(seed)):
        rot = []
        rot.append(seed[i])
        match = False
        # Every structures every cube, is multiplied by the rotation matrix
        # 3 times. These 3 new structures are than added to the "rot" list.
        for i in range(3):
            struct = []
            theta = np.radians((i+1)*90)
            c, s = np.cos(theta), np.sin(theta)
            R = np.matrix([[c, -s, 0],
                           [s,  c, 0],
                           [0,  0, 1]])
            for j in range(len(seed[i])): #for all cubes (/vectors)
                matrix = np.matmul(seed[i][j], R).astype(int)
                array = np.array(matrix)
                squeezed = np.squeeze(array).tolist()
                struct.append(squeezed)

            rot.append(struct)
            # Shift all 4 atructures to the first octant without filtering.
            rot = translation_filter(rot, False)
        seed[i].sort(key=lambda row: (row[0], row[1], row[2]))
        # If any of the rotated structures match an item in "result",
        # that means that there is a rotated version of the original structure
        # in "result". In this case we do not append them.
        for k in range(len(rot)):
            if rot[k] in result:
                match = True
            else:
                pass
        if not match:
            result.append(seed[i])
        
    seed.sort()
    # print(rot)
    print(len(result))
    return result


def create_plot_arrays(final_result):

    plt.ion()
    # prepare some coordinates
    x, y, z = np.indices((5, 5, 5))

    f_r = final_result
    vox_list = []

    for n in range(len(f_r)):
        # draw cuboids in the plot
        cube1 = (x == f_r[n][0][0]) & (y == f_r[n][0][1]) & (z == f_r[n][0][2])
        cube2 = (x == f_r[n][1][0]) & (y == f_r[n][1][1]) & (z == f_r[n][1][2])
        cube3 = (x == f_r[n][2][0]) & (y == f_r[n][2][1]) & (z == f_r[n][2][2])
        cube4 = (x == f_r[n][3][0]) & (y == f_r[n][3][1]) & (z == f_r[n][3][2])
        cube5 = (x == f_r[n][4][0]) & (y == f_r[n][4][1]) & (z == f_r[n][4][2])
        cube6 = (x == f_r[n][5][0]) & (y == f_r[n][5][1]) & (z == f_r[n][5][2])
        # combine the objects into a single boolean array
        voxels = cube1 | cube2 | cube3 | cube4 | cube5 | cube6

        colors = np.empty(voxels.shape, dtype=object)
        colors[:] = 'green'

        vox_list.append(voxels)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for n in range(len(f_r)):
        # and plot everything
        ax.voxels(vox_list[n])
        plt.pause(0.5)
        plt.cla()
    plt.show()

def create(origin, number_of_blocks):
    """Create all posible structures."""
    i = 0
    for i in range(number_of_blocks):
        origin = cuber(origin)
    return origin

def write_result(result):
    """Creates a CSV file with the structeres."""
    with open('result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)

########################################################################
# Function calls:                                                      #
# The input has to be the same format as the output: 3D matrix (list). #
########################################################################

origin = [[[0, 0, 0]]]
six_blocks = create(origin, 5)
all_connected = check_cube_connection(six_blocks)
two_on_floor = two_on_floor(all_connected)
max_1_balcony = balcony(two_on_floor)
offset_cubes = translation_filter(max_1_balcony, True)
less_than_four = four_in_line(offset_cubes)
final_result = rotaion_filter(less_than_four)

write_result(final_result)

create_plot_arrays(less_than_four)
