__author__ = 'longqi'

"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
# fig.set_size_inches(10.5, 10.5)
big_radius = 4
small_radius = big_radius / 2
ax.set_xlim(-big_radius, big_radius)
ax.set_ylim(-big_radius, big_radius)

x0 = np.arange(-big_radius, big_radius, 0.01)  # x0-array for big  cycle

# draw the big cycle
cycle0_line0, cycle0_line1 = ax.plot(x0, np.sqrt(big_radius * big_radius - x0 * x0), x0, 0 - np.sqrt(16 - x0 * x0))
plt.setp(cycle0_line0, color='r')

# draw two lines first
line0 = ax.plot(x0, x0 - x0)
line1 = ax.plot(x0 - x0, x0)

# the angle we will use
a0 = np.arange(0, 2 * np.pi, 0.1)  # a-array for small  cycle

dot0_angle = 0
dot1_angle = np.pi * 1 / 6
dot2_angle = np.pi * 2 / 6
dot3_angle = np.pi * 3 / 6
dot4_angle = np.pi * 4 / 6
dot5_angle = np.pi * 5 / 6
dot6_angle = np.pi * 6 / 6




# t = np.range
dot0, dot1, dot2, dot3, dot4, dot5, dot6 = ax.plot(0, 0, 'or',
                                                   0, 0, 'or',
                                                   0, 0, 'or',
                                                   0, 0, 'or',
                                                   0, 0, 'or',
                                                   0, 0, 'or',
                                                   0, 0, 'or')


def animate(epsilon):
    dot0.set_xdata(2 * small_radius * np.cos(epsilon - dot0_angle) * np.cos(dot0_angle))  # update the data
    dot0.set_ydata(2 * small_radius * np.cos(epsilon - dot0_angle) * np.sin(dot0_angle))  # update the data

    dot1.set_xdata(2 * small_radius * np.cos(epsilon - dot1_angle) * np.cos(dot1_angle))  # update the data
    dot1.set_ydata(2 * small_radius * np.cos(epsilon - dot1_angle) * np.sin(dot1_angle))  # update the data

    dot2.set_xdata(2 * small_radius * np.cos(epsilon - dot2_angle) * np.cos(dot2_angle))  # update the data
    dot2.set_ydata(2 * small_radius * np.cos(epsilon - dot2_angle) * np.sin(dot2_angle))  # update the data

    dot3.set_xdata(2 * small_radius * np.cos(epsilon - dot3_angle) * np.cos(dot3_angle))  # update the data
    dot3.set_ydata(2 * small_radius * np.cos(epsilon - dot3_angle) * np.sin(dot3_angle))  # update the data

    dot4.set_xdata(2 * small_radius * np.cos(epsilon - dot4_angle) * np.cos(dot4_angle))  # update the data
    dot4.set_ydata(2 * small_radius * np.cos(epsilon - dot4_angle) * np.sin(dot4_angle))  # update the data

    dot5.set_xdata(2 * small_radius * np.cos(epsilon - dot5_angle) * np.cos(dot5_angle))  # update the data
    dot5.set_ydata(2 * small_radius * np.cos(epsilon - dot5_angle) * np.sin(dot5_angle))  # update the data

    dot6.set_xdata(2 * small_radius * np.cos(epsilon - dot6_angle) * np.cos(dot6_angle))  # update the data
    dot6.set_ydata(2 * small_radius * np.cos(epsilon - dot6_angle) * np.sin(dot6_angle))  # update the data

    return dot0, dot1, dot2, dot3, dot4, dot5, dot6


# Init only required for blitting to give a clean slate.
def init():
    return dot0, dot1, dot2, dot3, dot4, dot5, dot6


ani = animation.FuncAnimation(fig, animate, np.arange(0, 2 * np.pi, 0.1), init_func=init,
                              interval=20, blit=False)

fig.show()
plt.show()
