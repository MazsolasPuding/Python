def river_measure(graph):
    minimum_island_size = len(graph) * len(graph[0])
    visited = set()

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == "L" or (row, col) in visited:
                island_size = depth_search(graph, (row, col), visited)
                if island_size < minimum_island_size and island_size != 0:
                    minimum_island_size = island_size
    return minimum_island_size


def depth_search(graph, coord, visited):
    row, col = coord
    if (row < 0 or
        col < 0 or
        row >= len(graph) or
        col >= len(graph[row]) or
        coord in visited or
        graph[row][col] == "W"): return 0

    visited.add(coord)

    size = 1

    a = depth_search(graph, (row+1, col), visited)
    b = depth_search(graph, (row-1, col), visited)
    c = depth_search(graph, (row, col+1), visited)
    d = depth_search(graph, (row, col-1), visited)
    size += a + b + c + d
    return size



def main():
    graph = [
        ["L", "W", "W", "W", "L"],
        ["L", "W", "L", "L", "L"],
        ["L", "W", "L", "W", "W"],
        ["L", "L", "W", "L", "L"],
        ["W", "L", "W", "L", "W"],
        ["W", "L", "W", "L", "L"]
    ]

    return river_measure(graph)

if __name__ == "__main__":
    res = main()
    print(res)