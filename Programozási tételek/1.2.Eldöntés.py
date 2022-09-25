from random_num import RandNum

class Eldontes:
    """Eldönti van-e adott tulajdonságú elem a tömbben."""

    def paros_e(self, rng, volume):
        """Megvizsgálja van-e páros szám a tömbben."""
        tomb = RandNum().generate(rng, volume)
        i = 0
        print(tomb)
        while i <= len(tomb) and not (tomb[i] % 2 == 0):
            i += 1
            if i >= len(tomb):
                break
        
        van = (i < len(tomb))
        return van

print(Eldontes().paros_e(100, 2))