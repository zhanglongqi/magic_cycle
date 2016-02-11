#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 11/Feb/16 10:27

A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
big_radius = 4
small_radius = big_radius / 2
ax.set_xlim(-big_radius, big_radius)
ax.set_ylim(-big_radius, big_radius)

x0 = np.arange(-big_radius, big_radius, 0.01)  # x0-array for big  cycle

# draw the big cycle
cycle0_line0, cycle0_line1 = ax.plot(x0, np.sqrt(big_radius ** 2 - x0 ** 2), x0, 0 - np.sqrt(big_radius ** 2 - x0 ** 2))
# plt.setp(cycle0_line0, color='r')

dots_angles = []
dots_num = 12
for i in range(0, dots_num):
    dots_angles.append(np.pi * i / dots_num)

# lines showing the path of dots moving
lines = []
for i in range(0, dots_num):
    y0 = np.multiply(x0, np.tan(dots_angles[i]))
    lines.append(ax.plot(x0, y0))

# dots moving in the plot
dots = []
for i in range(0, dots_num):
    dot, = ax.plot(0, 0, 'or')
    dots.append(dot)


def animate(epsilon):
    for i in range(0, dots_num):
        dots[i].set_xdata(
            2 * small_radius * np.cos(epsilon - dots_angles[i]) * np.cos(dots_angles[i]))  # update the data
        dots[i].set_ydata(
            2 * small_radius * np.cos(epsilon - dots_angles[i]) * np.sin(dots_angles[i]))  # update the data

    return dots


# Init only required for blitzing to give a clean slate.
def init():
    return dots


ani = animation.FuncAnimation(fig, animate, np.arange(0, 2 * np.pi, 0.1), init_func=init,
                              interval=10, blit=False)

ani._interval = 100
fig.show()
plt.show()
