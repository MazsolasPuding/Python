def count_islands(graph):
    visited = set()
    island_count = 0

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == "L":
                # print(f"Found: {row}, {col}")
                if (depth_search(graph, (row, col), visited)):
                    island_count += 1
                    # print(visited)

    return island_count


def depth_search(graph, source, visited):
    row, col = source
    if (col < 0 or
        row < 0 or
        row >= len(graph) or
        col >= len(graph[row]) or
        source in visited or
        graph[row][col] != "L"): return False
    
    # print(source)
    visited.add(source)

    depth_search(graph, (row, col-1), visited)
    depth_search(graph, (row-1, col), visited)
    depth_search(graph, (row, col+1), visited)
    depth_search(graph, (row+1, col), visited)
    
    return True



def main():
    graph = [
        ["L", "W", "W", "W", "L"],
        ["L", "W", "L", "L", "L"],
        ["L", "W", "L", "W", "W"],
        ["L", "L", "L", "L", "L"],
        ["W", "L", "W", "L", "W"],
        ["W", "L", "W", "L", "L"]
    ]

    return count_islands(graph)

if __name__ == "__main__":
    res = main()
    print(res)
