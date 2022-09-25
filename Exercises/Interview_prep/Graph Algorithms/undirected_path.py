def undirected_graph(edges, source, dest):
    graph = make_graph(edges)
    print(graph)
    return breadth_first(graph, source, dest, set())


def depth_first(graph, source, dest, visited):
    if source == dest: return True
    if source in visited: return False
    visited.add(source)

    for neighbour in graph[source]:
        if depth_first(graph, neighbour, dest, visited):
            return True
    return False


def breadth_first(graph, source, dest, visited):
    queue = [source]

    while queue:
        current = queue.pop(0)
        
        if current == dest: return True
        if current in visited: continue
        visited.add(current)

        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


# {
#   'i': ['j', 'k'],
#   'j': ['i'],
#   'k': ['i', 'm', 'l'],
#   'm': ['k'],
#   'l': ['k'],
#   'o': ['n'],
#   'n': ['o']
# }


def make_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        graph[a].append(b)
        if b not in graph: graph[b] = []
        graph[b].append(a)
    return graph


def main():
    edges = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"]
    ]

    return undirected_graph(edges, "i", "m")


if __name__ == "__main__":
    res = main()
    print(res)