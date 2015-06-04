__author__ = 'longqi'

"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
# fig.set_size_inches(10.5, 10.5)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

x0 = np.arange(-4, 4, 0.01)  # x0-array for big  cycle

# draw the big cycle
cycle0_line0, cycle0_line1 = ax.plot(x0, np.sqrt(16 - x0 * x0), x0, 0 - np.sqrt(16 - x0 * x0))
plt.setp(cycle0_line0, color='r')

# draw two lines first
line0 = ax.plot(x0, x0 - x0)
line1 = ax.plot(x0 - x0, x0)

# the angle we will use
a0 = np.arange(0, 4 * np.pi, 0.01)  # a-array for small  cycle

dot0, = ax.plot(a0 - a0 + 1, a0)


def animate(i):
    dot0.set_ydata(i)  # update the data

    return dot0,


# Init only required for blitting to give a clean slate.
def init():
    dot0.set_ydata(np.ma.array(a0, mask=True))
    return dot0,


ani = animation.FuncAnimation(fig, animate, np.arange(0, np.pi, 0.1), init_func=init,
                              interval=25, blit=False)

fig.show()
plt.show()
