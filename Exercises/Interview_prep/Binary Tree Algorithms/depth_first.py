class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# def depth_first(root):
#     if root == None: return []
#     stack = [root]
#     result = []
#     while stack:
#         current = stack.pop()
#         result.append(current.value)

#         if current.right: stack.append(current.right)
#         if current.left: stack.append(current.left)

#     return result


def depth_first(root):
    if root == None: return []
    left_values = depth_first(root.left) # returns [b, d, e]
    right_values = depth_first(root.right) # returns [c, f]
    return [root.value, *left_values, *right_values]



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

    return depth_first(a)


if __name__ == "__main__":
    res = main()
    print(res)