import pprint

class FindPath:
	def __init__(self, graph: list, start: tuple, target: tuple) -> int:
		self.graph = graph
		self.start = start
		self.target = target

	def path_finder(self):
		visited = []
		path_length = self.breadth_search(visited)
		return path_length

	def breadth_search(self, visited: list) -> int:
		queue = [(*self.start, 0)]

		while queue:
			current = queue.pop(0)
			row, col, path_len = current

			if (row < 0 or
				col < 0 or
				row >= len(self.graph) or
				col >= len(self.graph[row]) or
				(row, col) in visited or
				self.graph[row][col] == "X"):
				continue
			elif (row, col) == self.target:
				return path_len

			print(current, " : ", self.graph[row][col])
			visited.append((row, col))
			self.graph[row][col] = path_len

			queue.append((row-1, col, path_len+1))
			queue.append((row, col-1, path_len+1))
			queue.append((row+1, col, path_len+1))
			queue.append((row, col+1, path_len+1))
		return 0


def main() -> None:
	graph = [
        ["X", 0, 0, 0, 0],
        ["S", 0, "X", 0, 0],
        [0, 0, "X", 0, 0],
        [0, 0, "X", "T", 0],
        [0, 0, "X", 0, 0],
        ["X", 0, 0, 0, 0]
    ]
	start = (1, 0)
	target = (3, 3)
	fp = FindPath(graph, start, target)
	path_length = fp.path_finder()
	print(path_length)
	pprint.pprint(graph)

if __name__ == "__main__":
	main()

