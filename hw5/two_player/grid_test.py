import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')
patch1 = plt.Circle((5, -5), 0.75, fc='b')

def init():
    patch.center = (5, 5)
    patch1.center = (1, 1)
    ax.add_patch(patch)
    ax.add_patch(patch1)
    return patch, patch1

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    patch1.center = (1, 1)
    if i%2 == 0:
      patch.set_fc('y')
    else: 
      patch.set_fc('r')
    return patch, patch1

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
