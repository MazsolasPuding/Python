import sys
sys.path.append('./../')
import Python.Exercises._2022_Fall.fizz_buzz as fb
import unittest
import random

class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        arr = []
        while len(arr) <= 5:
            rand_num = random.randint(1, 100)
            if rand_num % 3 == 0 and not rand_num % 5 == 0:
                arr.append(rand_num)

        # print(f'fizz: {arr}')
        for num in arr:
            self.assertEqual(fb.fizz_buzz(num-1), 'Fizz')

    def test_buzz(self):
        arr = []
        while len(arr) <= 5:
            rand_num = random.randint(1, 100)
            if not (rand_num % 3 == 0) and rand_num % 5 == 0:
                arr.append(rand_num)

        # print(f'buzz: {arr}')
        for num in arr:
            self.assertEqual(fb.fizz_buzz(num-1), 'Buzz')

    def test_fizzbuzz(self):
        arr = []
        while len(arr) <= 5:
            rand_num = random.randint(1, 100)
            if rand_num % 3 == 0 and rand_num % 5 == 0:
                arr.append(rand_num)

        # print(f'fizzbuzz: {arr}')
        for num in arr:
            self.assertEqual(fb.fizz_buzz(num-1), 'FizzBuzz')
    
    def test_num(self):
        arr = []
        while len(arr) <= 5:
            rand_num = random.randint(1, 100)
            if not (rand_num % 3 == 0) and not (rand_num % 5 == 0):
                arr.append(rand_num)

        for num in arr:
            self.assertEqual(fb.fizz_buzz(num-1), str(num))


if __name__ == '__main__':
    unittest.main()

