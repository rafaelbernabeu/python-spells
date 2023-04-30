import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x = np.arange(0, 10, 0.005)
y = np.sin(x)

zero = [0 for x in range(len(x))]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, zero)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

plt.show()