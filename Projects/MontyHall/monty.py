"""Monty hall problem:
    - 3 Doors: 000 -> 2 goat 1 car -> 00X (x = car, 0 = goat)
    - Random selection: 010 (1 = selected)
    - Monty shows door[0] = 0 (a goat)
    - participant switches: from door[1] to door[2]
"""

import random

class montyHall:
    def __init__(self):
        self.generate_pick()
        self.generate_switch_pick()

    def generate_switch_pick(self):
        pool = [0, 0, 'X']
        random.shuffle(pool)
        print(pool)
        pick = random.choice(range(3))
        pick_value = pool[pick]
        car_location = pool.index('X')
        print(pick)
        print(pick_value)
        open_door = self.monty_opens_the_fucking_door(pick, pick_value, car_location)
        
        final_choice = list(range(3))
        final_choice.remove(open_door)
        final_choice.remove(pick)
        print(f"final chouce: {final_choice[0]} = {pool[final_choice[0]]}")
        return pool[final_choice[0]]


    def generate_pick(self):
        pass

    def monty_opens_the_fucking_door(self, pick, pick_value, car_location):
        if pick_value == 0:
            open_door = list(range(3))
            open_door.remove(pick)
            open_door.remove(car_location)
            print(open_door[0])
            return open_door[0]
        else:
            open_door = list(range(3))
            open_door.remove(pick)
            open_door = random.choice(open_door)
            print(open_door)
            return open_door


if __name__ == "__main__":
    monty = montyHall()
