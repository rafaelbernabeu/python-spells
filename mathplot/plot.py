from random import random
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = 56654

for i in range(0, 10_000_000):

    if (x % 2) == 0:
        x = int(x / 2)
    else:
        x = int(3 * x + 1)

    print(x)
    ax.plot(i, x, 'o')
    #ax.plot(int(random() * 100), int(random() * 100), 'o')

    if x == 1 :
        break


plt.show()