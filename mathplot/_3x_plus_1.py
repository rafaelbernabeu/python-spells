import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def _3x_plus_1(param):
    ret = [param]
    while True:
        x = ret[len(ret) - 1]
        if (x % 2) == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
        ret.append(x)
        if x == 1:
            break

    return ret



(fig, ax) = plt.subplots()
plt.suptitle("3x+1")

biggestIdx = 0
biggestResult = 0
data = [x+int(random.randbytes(2).hex(), 16) for x in range(10_000)]  

def update(frame):
    global fig, ax, biggestIdx, biggestResult
    ax.clear()
    result = _3x_plus_1(frame)
    if (max(result) > biggestResult):
       biggestResult = max(result)
       biggestIdx = frame
    line = ax.plot(range(0, len(result)), result)[0]
    ax.add_line(line)
    ax.set_xlabel(f'X={frame} Mean={int(np.mean(result))} Max={max(result)} GlobalMax=( X={biggestIdx} | {biggestResult} )')
    return fig

ani = animation.FuncAnimation(fig=fig, func=update, frames=data, interval=500)
plt.show()