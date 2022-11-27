from pprint import pprint

# def generate_maze(N):
#     for i in range(N):
#         row = ''
#         for j in range(N):
#             if i == 0 or i == N-1:
#                 row += '#'
#             elif j == 0 or j == N-1:
#                 row += '#'
#             else:
#                 row += 'O'
#         print(row)

def generate_field(N):
    field = []
    for i in range(N):
        row = ['#'] * N
        if (i == 1):
            row[0] = 'S'
        elif (i == 2):
            row[0] = 'E'
        for j in row:
            pass
        field.append(row)
    return field

def robot_mouse(N, field):
    current = (1, 0)
    directions = ['right', 'down', 'left', 'up']
    visited = set()
    cnt = N
    while cnt:
        for direction in directions:
            while True:
                next_pos = move(N, field, current, direction)
                if next_pos:
                    current = next_pos
                    field[current[0]][current[1]] = ' '
                else:
                    break
        cnt -= 1
    return field

def move(N, field, coord, direction):
    if direction == 'right':
        if coord[1]+2 < N and field[coord[0]][coord[1]+2] == '#':
            return (coord[0], coord[1]+1)
    elif direction == 'down':
        if coord[0]+2 < N and field[coord[0]+2][coord[1]] == '#':
            return (coord[0]+1, coord[1])
    elif direction == 'left':
        if coord[1]-2 >= 0 and field[coord[0]][coord[1]-2] == '#':
            return (coord[0], coord[1]-1)
    elif direction == 'up':
        if coord[0]-2 >= 0 and field[coord[0]-2][coord[1]] == '#':
            return (coord[0]-1, coord[1])
    else:
        return False


        


# def wall_counter(N, field, coord):
#     row, col = coord
#     count = 0
#     if (row-1 < 0 or
#         col-1 < 0 or
#         row+1 >= N or
#         col+1 >= N): return 0

#     if field[row][col+1] == '#':
#         count += 1
#     if field[row+1][col] == '#':
#         count += 1
#     if field[row][col-1] == '#':
#         count += 1
#     if field[row-1][col] == '#':
#         count += 1
#     print(count)
#     return count


# def depth_search(N, field, coord, visited):
#     row, col = coord
#     if (row < 0 or
#         col < 0 or
#         row >= N or
#         col >= N or
#         coord in visited or
#         field[row][col] == '0'): return 0

#     visited.add(coord)
#     field[row][col] = '0'
#     pprint(field)
    

#     right = depth_search(N, field, (row, col+1), visited)
#     down = depth_search(N, field, (row+1, col), visited)
#     left = depth_search(N, field, (row, col-1), visited)
#     up = depth_search(N, field, (row-1, col), visited)
    

#     # if right:
#     #     field[row][col] = '0'
#     return True



# generate_maze(15)
N = 15
field = generate_field(N)
# pprint(field)
maze = robot_mouse(N, field)
pprint(field)
# for line in maze:
#     print(''.join(line))