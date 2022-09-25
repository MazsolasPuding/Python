def has_path_depth_first(graph, src, dst):
  print(src)
  if src == dst: return True
  
  for neighbour in graph[src]:
    if (has_path_depth_first(graph, neighbour, dst)):
      return True
  return False
    

def has_path_breadth_first(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop(0)
        print(current)
        if current == dst: return True

        for neighbour in graph[current]:
            queue.append(neighbour)
    return False



def main():
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    res_1 = has_path_depth_first(graph, "f", "k")
    print()
    res_2 = has_path_breadth_first(graph, "f", "k")
    print(res_1, res_2)

if __name__ == "__main__":
    main()