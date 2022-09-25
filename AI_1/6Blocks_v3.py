"""Generate and visualize the 6Blocks problem."""

import numpy

"""
Generate all possible structure variatons from 6 Blocks by the following rules.
- Minimum 2 blocks on the ground.
- All blocks joined (on surfaces).
- Max 1 balcony (overhang).
- Max 3 blocks height.
- Max 4 blocks in a singal straight line.
"""


class SixBlocks:
    """Overall class to manage assetts."""

    def __init__(self):
        """Initialize the prgrame and create reosurcers."""
        self.space = []
        self.x = 4
        self.y = 3
        self.z = 3

        self.count = 0

    def run_algorithm(self):
        """Start running the generator."""
        self._create_enviroment()
        self._init_starting_position()
        self._print_current()
        self.generate()

    def _create_enviroment(self):
        """Create the 3D space array"""
        self.x = 4
        self.y = 3
        self.z = 3
        self.space = numpy.zeros((self.x, self.y, self.z), dtype=int)

    def _init_starting_position(self):
        """Set up the starting positions of the blocks"""
        self.space[0][0][0] = 1
        self.space[0][0][1] = 1
        self.space[0][0][2] = 1
        self.space[0][1][0] = 1
        self.space[0][1][1] = 1
        self.space[0][1][2] = 1

    def generate(self):
        num = 0
        n = 0
        old_p = []
        for y in range(2):
            for z in range(self.z):
                num = self.space[0][y][z]
                old_p = [0, 0, 0]
                n = 0
                self._position_index_loop(n, old_p)
        print(self.count)

    def _block_index_loop(self):
        """Cycle through each block in the 3D space."""
        num = 0
        n = 0
        old_p = []
        for y in range(2):
            for z in range(self.z):
                num = self.space[0][y][z]
                old_p = [0, 0, 0]
                n = 0

    def _position_index_loop(self, n, old_p):
        """
        Cycle through each possible position for the blocks in the 3D space.
        """
        for x1 in range(self.x):
            for y1 in range(self.y):
                for z1 in range(self.z):
                    n += 1
                    if self.space[x1][y1][z1] == 1:
                        old_p = [x1, y1, z1]
                        pass
                    else:
                        if n > 7:
                            self.space[old_p[0]
                                       ][old_p[1]][old_p[2]] = 0
                        self.space[x1][y1][z1] = 1
                        self.count += 1
                        print(self.space)
                        print()
                        old_p = [x1, y1, z1]
                        print(old_p)
                        print()

    def _print_current(self):
        print(self.space)


if __name__ == '__main__':
    sb = SixBlocks()
    sb.run_algorithm()
