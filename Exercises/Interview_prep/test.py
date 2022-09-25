# import time
# import pprint
# import itertools

# class cycler:
#     """Cycling char."""

#     def __init__(self, filler=".", cycling_char="0"):
#         self.filler = filler
#         self.cycling_char = cycling_char

#     def _background(self):
#         sub_arr = [self.filler] * 5
#         bg = [sub_arr[:] for i in range(5)]
#         return bg
        
#     def insert_cycling_char(self):
#         coords = [
#             (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)
#             ]
#         for coord in itertools.cycle(coords[::-1]):
#             bg = self._background()
#             x, y = coord
#             bg[y][x] = str(0)
#             print(bg[y][x])
#             pprint.pprint(bg)
#             time.sleep(0.2)


# if __name__ == "__main__":
#     loading_screen = cycler()
#     loading_screen.insert_cycling_char()


for i in range(6, 2, -1):
    print(i)
