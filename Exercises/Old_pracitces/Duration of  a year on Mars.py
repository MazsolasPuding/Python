Mars_R = 227.92 #[[MKm]]
Mars_R = Mars_R * 10**6

from math import pi
Mars_S = 2 * pi * Mars_R #[Km]
Mars_V = 24 #[Km/s]
Mars_T = Mars_S / Mars_V #[S]
print(Mars_T)

Mars_D = Mars_T / (60 * 60 * 24) #[Nap]
print(str(Mars_D) + " Földi nap a Mars keringési ideje.")