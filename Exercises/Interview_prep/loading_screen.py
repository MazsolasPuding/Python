import random

from numpy import array

class lists:
    """Methods and tricks with lists."""

    def __init__(self, length=10, num_range=(0, 10)):
        self.length = length
        self.num_range = num_range
        self.array = [random.randint(*num_range) for x in range(0, length)]
    
    def unique_elems(self):
        return print(len(set(self.array)))

    def print_array_len(self):
        print(self.array)
        return print(len(self.array))



if __name__ == "__main__":
    list_1 = lists(10)
    list_1.print_array_len()
    list_1.unique_elems()