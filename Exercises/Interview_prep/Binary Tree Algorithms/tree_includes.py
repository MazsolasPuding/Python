class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth_first_includes(root, target):
    if root == None: return False
    stack = [root]

    while stack:
        current = stack.pop()
        print(current.value)
        if current == target: return True

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return False


def depth_first_includes_recursive(root, target):
    if root == None: return False
    print(root.value)
    if root == target: return True
    return (depth_first_includes_recursive(root.left, target) or
            depth_first_includes_recursive(root.right, target))


def breadth_first(root, target):
    if root == None: return False
    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.value)
        if current == target: return True
        
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False



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

    depth = depth_first_includes(a, e)
    print()
    depth_rec = depth_first_includes_recursive(a, e)
    print()
    breadth = breadth_first(a, e)

    return [depth, depth_rec, breadth]

if __name__ == "__main__":
    res = main()
    print(res)