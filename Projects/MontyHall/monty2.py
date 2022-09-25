"""Monty hall problem:
    - 3 Doors: 000 -> 2 goat 1 car -> 00X (x = car, 0 = goat)
    - Random selection: 010 (1 = selected)
    - Monty shows door[0] = 0 (a goat)
    - participant switches: from door[1] to door[2]
"""

import random

class montyHall:
    def __init__(self):
        self.pool = [0, 0, 'X']

    def generate_pick(self):
        pick = random.choice(range(3))
        # print(pool)
        # print(pool[pick])
        return self.pool[pick]

    def generate_switch_pick(self):
        pick = random.choice(range(3))
        open_door = self.monty_opens_the_fucking_door(pick)
        final_choice = list(range(3))
        final_choice.remove(open_door)
        final_choice.remove(pick)
        # print(self.pool)
        # print(pick)
        # print(f"final chouce: {final_choice[0]} = {self.pool[final_choice[0]]}")
        return self.pool[final_choice[0]]

    def monty_opens_the_fucking_door(self, pick):
        if pick == 2:
            return random.choice(range(2))
        elif pick == 0:
            return 1
        return 0


if __name__ == "__main__":
    monty = montyHall()
    cycles = 10000000
    regular_picks = [monty.generate_pick() for x in range(cycles)]
    rate = regular_picks.count('X')/cycles*100
    print(f"\nRegular picks success rate: {round(rate, 3)}%")

    switch_picks = [monty.generate_switch_pick() for x in range(cycles)]
    rate = switch_picks.count('X')/cycles*100
    print(f"Switch picks success rate: {round(rate, 3)}%\n")

