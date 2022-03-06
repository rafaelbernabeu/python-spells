from random import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 1000)

fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x), animated=True)
ax.autoscale = True
ax.grid()

plt.show(block=False)
plt.pause(0.1)

bg = fig.canvas.copy_from_bbox(fig.bbox)
ax.draw_artist(line)
fig.canvas.blit(fig.bbox)


for j in range(1000):
    # reset the background back in the canvas state, screen unchanged
    fig.canvas.restore_region(bg)
    # update the artist, neither the canvas state nor the screen have changed
    line.set_ydata(np.sin(x + (j / 100) * np.pi))
    # re-render the artist, updating the canvas state, but not the screen
    ax.draw_artist(line)
    # copy the image to the GUI state, but screen might not be changed yet
    fig.canvas.blit(fig.bbox)
    # flush any pending GUI events, re-painting the screen if needed
    fig.canvas.flush_events()
    # you can put a pause in if you want to slow things down
    # plt.pause(.1)

def animate(x) :
    print(x)
    if (x % 2) == 0:
        x = int(x / 2)
    else:
        x = int(3 * x + 1)
    