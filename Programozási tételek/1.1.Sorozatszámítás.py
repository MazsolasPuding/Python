from random_num import RandNum

class Sorozatszamitas:
    """Egy tömb összes eleme között elvégez egy adott műveletet."""

    def sorozatszamitas_osszeg(self, rng, volume):
        """Egy tömb összes elemét összegzi."""
        tömb = RandNum().generate(rng, volume)
        érték = 0

        for i in range(len(tömb)):
            érték += tömb[i]
        
        return érték
    
    def sorozatszamitas_szorzat(self, rng, volume):
        """Egy tömb összes elemét összegzi."""
        tömb = RandNum().generate(rng, volume)
        érték = 1

        for i in range(len(tömb)):
            érték *= tömb[i]
        
        return érték

print(Sorozatszamitas().sorozatszamitas_osszeg(50, 10))
print(Sorozatszamitas().sorozatszamitas_szorzat(50, 10))