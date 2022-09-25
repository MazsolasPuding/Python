
def largest_component(graph):
    visited = set()
    total_max = 0

    for node in graph:
        current_max = depth_search(graph, node, visited)
        if current_max > total_max:
            total_max = current_max
    return total_max
            



def depth_search(graph, source, visited):
    if source in visited: return 0
    visited.add(source)
    local_sum = 1

    for neighbor in graph[source]:
        local_sum += depth_search(graph, neighbor, visited)

    return local_sum


def breadth_search(graph, source, visited):
    queue = [source]
    local_sum = 0

    while queue:
        current = queue.pop(0)
        if current not in visited:
            local_sum += 1
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
    return local_sum



def main():
    graph = {
        0: [1, 5, 8],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3],
        5: [0, 8],
        8: [5, 0]
    }

    

    return largest_component(graph)

if __name__ == "__main__":
    res = main()
    print(res)
