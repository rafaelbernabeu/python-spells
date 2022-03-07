import numpy as np
import matplotlib.pyplot as plt


def _3x_plus_1(param):
    ret = [param]
    while True:
        x = ret[len(ret) - 1]
        print(x)
        if (x % 2) == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
        ret.append(x)
        if x == 1:
            break

    return ret


(fig, ax) = plt.subplots()

xData = np.random.random(20) * 1000
lines = []

for i in xData:
    result = _3x_plus_1(int(i))
    line, = ax.plot(range(0, len(result), 1), result, label=int(i))
    lines.append(line)

legend = ax.legend(handles=lines, loc='upper right')

plt.show()
