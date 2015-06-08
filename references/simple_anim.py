"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.1)  # x0-array
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i))  # update the data
    print(line.get_ydata())
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, 20, 0.1), init_func=init,
                              interval=25, blit=False)
plt.show()
