
def connected_count(graph):
    visited = set()
    connected_component_count = 0
    for node in graph:
        if node not in visited:
            connected_component_count += 1
            # depth_first(graph, node, visited)
            breadth_first(graph, node, visited)

    return connected_component_count


def depth_first(graph, source, visited):
    if source in visited: return True
    visited.add(source)

    for neighbor in graph[source]:
        depth_first(graph, neighbor, visited)
    return True
    

def breadth_first(graph, source, visited):
    queue = [source]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append(neighbor)

    return True



def main():
    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }

    

    return connected_count(graph)

if __name__ == "__main__":
    res = main()
    print(res)