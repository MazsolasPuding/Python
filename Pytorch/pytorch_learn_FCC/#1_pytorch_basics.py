import torch
import torch as t
import numpy as np
import pprint

pp = pprint.PrettyPrinter(indent=4)


def list_range(lower: int = 0, upper: int = 0) -> int:
    return list(range(lower, upper))


def tensor_ops():
    list_1 = list(range(10))
    t1 = t.tensor(1.)
    t2 = t.tensor(list_1)
    t3 = t.tensor([[list(range(2))],
                   [list(range(2, 4))],
                   [list(range(4, 6))]])
    pp.pprint(t3)

    x = torch.tensor(3.)
    w = torch.tensor(4., requires_grad=True)
    b = torch.tensor(5., requires_grad=True)
    print(x, w, b)

    # Arithmetics
    y = w * x + b
    print(y)

    # Compute y's derivative
    print(y.backward())


if __name__ == '__main__':
    tensor_ops()
