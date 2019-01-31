import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from sim_paths import * 
import os 

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(16, 4)

ax = plt.axes(xlim=(0, 4), ylim=(0, 1))
patch_h = plt.Circle((1, 1), 0.1, fc='g')
patch_r = plt.Circle((1, 1), 0.1, fc='y')

def mapping(states_one_step):
    # human 

    if states_one_step[1] == 1:
      patch_h.set_fc('r')
    else: 
      patch_h.set_fc('g')
    if states_one_step[0] == 0:
      patch_h.center = (0.5, 0.5)
    else: 
      patch_h.center = (1.48, 0.5)
    # human 
    if states_one_step[3] == 1:
      patch_r.set_fc('m')
    else: 
      patch_r.set_fc('y')
    if states_one_step[2] == 1:
      patch_r.center = (1.52, 0.5)
    elif states_one_step[2] == 2: 
      patch_r.center = (2.5, 0.5)
    else: 
      patch_r.center = (3.5, 0.5)
    return patch_h, patch_r

def init():

    states_init = var_list[0]
    patch_h, patch_r = mapping(states_init)
    ax.add_patch(patch_h)
    ax.add_patch(patch_r)
    return patch_h, patch_r

def animate(i):

    print "i", i 

    states_one_step = var_list[i]
    patch_h, patch_r = mapping(states_one_step)
    return patch_h,patch_r


dreamer_lookup = [
  {'name': 'h_state', 'bits': 2},
  {'name': 'h_closed', 'bits': 1},
  {'name': 'r_state', 'bits': 2},
  {'name': 'r_closed', 'bits': 1}
]

path_location = os.path.dirname(os.path.realpath(__file__))
dreamer_file = os.path.join(path_location, 'two_player', 'ctrl.json')
# dreamer_file = '/home/formal/cyberphysical_systems/hw5/two_player/ctrl.json'
dreamer_sim = Controller(dreamer_lookup, dreamer_file)
node_init = '0'
var_list = dreamer_sim.simulate(node_init, 40)



plt.fill([0,1,1,0], [0,0,1,1], 'b', alpha=0.2, edgecolor='r')
plt.fill([1,2,2,1], [0,0,1,1], 'y', alpha=0.2, edgecolor='r')
plt.fill([2,3,3,2], [0,0,1,1], 'b', alpha=0.2, edgecolor='r')
plt.fill([3,4,4,3], [0,0,1,1], 'y', alpha=0.2, edgecolor='r')
plt.grid()


l = len(var_list)

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init(), 
                               frames=l, 
                               interval=1000,
                               blit=True,
                               repeat=False)


# Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# anim.save('dreamer_two_player.mp4')
plt.show()