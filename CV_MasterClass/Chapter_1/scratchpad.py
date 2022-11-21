import math
import numpy as np
import matplotlib.pyplot as plt

upper_limit = math.pi*2
x = np.arange(0, upper_limit, 0.01)
y_0 = np.sin(x)
y_1 = np.sin(x-np.pi/2)
y_2 = np.sin(x+np.pi/2)

plt.plot([0, upper_limit], [0, 0], 'r--')
plt.plot(x, y_0, 'g')
plt.plot(x, y_1, 'b')
plt.plot(x, y_2, 'orange')

plt.show()