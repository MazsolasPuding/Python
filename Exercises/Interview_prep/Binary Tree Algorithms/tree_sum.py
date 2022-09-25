class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth_first(root):
    if root == None: return 0
    stack = [root]
    sum = 0

    while stack:
        current = stack.pop()
        sum += current.value
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return sum


def depth_first_recursive(root):
    if root == None: return 0
    sum = depth_first_recursive(root.left) + depth_first_recursive(root.right)
    sum += root.value
    return sum


def breadth(root):
    if root == None: return 0
    queue = [root]
    sum = 0

    while queue:
        current = queue.pop(0)
        sum += current.value
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum



def main():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    depth = depth_first(a)
    depth_rec = depth_first_recursive(a)
    bread = breadth(a)

    return [depth, depth_rec, bread]
    



if __name__ == "__main__":
    res = main()
    print(res)