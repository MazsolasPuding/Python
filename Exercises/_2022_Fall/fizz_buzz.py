import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import random
from pprint import pprint


def fizz_buzz(return_idx, lower_range=0, upper_range=100, print_list=False):
    """FizzBuzz from 1"""
    arr = [0] * (upper_range - lower_range)
    item = ''
    # print(f"length: {len(arr)}")
    for x, _ in enumerate(arr):
        if (x + 1) % 3 == 0:
            item += 'Fizz'
        if (x + 1) % 5 == 0:
            item += 'Buzz'
        if not (x + 1) % 3 == 0 and not (x + 1) % 5 == 0:
            item = str(x + 1)
        arr[x] = item
        item = ''
    
    if print_list:
        pprint(arr)

    return arr[return_idx]


if __name__ == '__main__':
    print(fizz_buzz(0, print_list=False))