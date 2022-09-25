"""Generating random numbers."""
from random import randint

class RandNum:
    """Generate a set of random numbers in a given range."""
     
    def generate(self, rng, volume):
        """Generate numbers in a given range into a list."""
        rand_nums = []
        n = 0
        while n < volume:
            r = randint(0, rng)
            rand_nums.append(r)
            n += 1

        return rand_nums
    
if __name__ == "__main__":
    rn = RandNum()
    print(rn.generate(20, 10))
