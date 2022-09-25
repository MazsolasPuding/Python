def river_measure(graph):
    longest_river = 0
    visited = set()

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == 1:
                reiver_length = depth_search(graph, (row, col), visited)
                if reiver_length > longest_river:
                    longest_river = reiver_length
    return longest_river


def depth_search(graph, coord, visited):
    row, col = coord
    if (row < 0 or
        col < 0 or
        row >= len(graph) or
        col >= len(graph[row]) or
        coord in visited or
        graph[row][col] == 0): return 0

    visited.add(coord)

    length = 1

    a = depth_search(graph, (row+1, col), visited)
    b = depth_search(graph, (row-1, col), visited)
    c = depth_search(graph, (row, col+1), visited)
    d = depth_search(graph, (row, col-1), visited)
    length += a + b + c + d
    return length



def main():
    graph = [
        [1, 0, 0, 0 , 0],
        [1, 1, 0, 1 , 1],
        [0, 0, 1, 1 , 0],
        [0, 0, 0, 0 , 0],
        [0, 0, 1, 0 , 1],
        [0, 1, 1, 0 , 0]
    ]

    return river_measure(graph)

if __name__ == "__main__":
    res = main()
    print(res)
    