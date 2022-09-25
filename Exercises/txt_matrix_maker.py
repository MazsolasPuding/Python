import random

def make_2D_matrix(row, col):
    matrix = []
    count = 0
    for i in range(row):
        row = []
        for j in range(col):
            row.append(random.uniform(-100, 100))
            count += 1
        matrix.append(row)
    print(count)
    return matrix


def write_matrix_to_file(matrix):
    with open('matrix.txt', 'w', newline='') as f:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                f.write(str(matrix[i][j])+'     ')
            f.write('\n')

mat = make_2D_matrix(5, 5)
write_matrix_to_file(mat)
