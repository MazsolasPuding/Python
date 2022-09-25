from numpy import Infinity


def shortest_path(graph, source, dest):
    queue = [(source, 0)]
    visited = set()
    step_count = 0

    while queue:
        print(queue)
        current = queue.pop(0)
        if current[0] == dest:
            return current[1]
        step_count = current[1] + 1


        if current[0] not in visited:
            visited.add(current[0])
            for neghbor in graph[current[0]]:
                queue.append((neghbor, step_count))
    return -1




def main():
    graph = {
        "w": ["x", "v"],
        "x": ["w", "y"],
        "y": ["x", "z"],
        "v": ["w", "z"],
        "z": ["y", "v"]
    }
    source = "y"
    dest = "v"
    # Return the shortest path from w to z
    return shortest_path(graph, source, dest)

if __name__ == "__main__":
    result = main()
    print(result)