class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(root):
    if root == None: return []
    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return result










def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return breadth_first(a)

if __name__ == "__main__":
    res = main()
    print(res)