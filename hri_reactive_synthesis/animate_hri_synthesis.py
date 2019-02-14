import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os 
import sys 

path_location = os.path.dirname(os.path.realpath(__file__))
sim_paths_location = os.path.join(path_location, '..') 
sys.path.insert(0, sim_paths_location)
import sim_paths

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(16, 4)

ax = plt.axes(xlim=(0, 4), ylim=(0, 1))
patch_h = plt.Circle((1, 1), 0.1, fc='g')
patch_r = plt.Circle((1, 1), 0.1, fc='y')
patch_O2 = plt.Circle((1, 1), 0.1, fc='r')
patch_O3 = plt.Circle((1, 1), 0.1, fc='r')

def mapping(states_one_step):

		# obstacle 2
		patch_O2.set_fc('r')
		if states_one_step[1] == 1:
			patch_O2.center = (1.5, 0.5)
		else: 
			patch_O2.center = (1.5, 0.9)
		# obstacle 3
		patch_O3.set_fc('r')
		if states_one_step[2] == 1:

			patch_O3.center = (2.5, 0.5)
		else: 
			patch_O3.center = (2.5, 0.9)

		# robot
		if states_one_step[13] == 1:
			patch_r.set_fc('c')
		else: 
			patch_r.set_fc('y')
		if states_one_step[10] == 0:
			patch_r.center = (0.5, 0.8)
		elif states_one_step[10] == 1: 
			patch_r.center = (0.5, 0.5)
		elif states_one_step[10] == 2: 
			patch_r.center = (1.5, 0.5)
		elif states_one_step[10] == 3: 
			patch_r.center = (2.5, 0.5)
		else:    
			patch_r.center = (3.48, 0.5)


		# human
		if states_one_step[8] == 0:
			patch_h.set_fc('k')
		elif states_one_step[4] == 1:
			patch_h.set_fc('b')
		else: 
			patch_h.set_fc('y')
		workload = states_one_step[3]
		patch_h.set_radius(.005 * workload)
		patch_h.center = (3.5, 0.5)

		return patch_h, patch_r, patch_O2, patch_O3

def init():

		states_init = var_list[0]
		patch_h, patch_r, patch_O2, patch_O3 = mapping(states_init)
		ax.add_patch(patch_h)
		ax.add_patch(patch_r)
		ax.add_patch(patch_O2)
		ax.add_patch(patch_O3)		

		return patch_h, patch_r, patch_O2, patch_O3

def animate(i):

		print "i", i 



		states_one_step = var_list[i]
		patch_h, patch_r, patch_O2, patch_O3 = mapping(states_one_step)
		return patch_h, patch_r, patch_O2, patch_O3



plt.fill([0,1,1,0], [0,0,1,1], 'b', alpha=0.2, edgecolor='r')
plt.fill([1,2,2,1], [0,0,1,1], 'y', alpha=0.2, edgecolor='r')
plt.fill([2,3,3,2], [0,0,1,1], 'b', alpha=0.2, edgecolor='r')
plt.fill([3,4,4,3], [0,0,1,1], 'y', alpha=0.2, edgecolor='r')
plt.grid()


delivery_lookup = sim_paths.get_lookup()

delivery_file = os.path.join(path_location, 'ctrl.json')
delivery_sim = sim_paths.Controller(delivery_lookup, delivery_file)
node_init = '0'
var_list = delivery_sim.simulate(node_init, 60)


l = len(var_list)

anim = animation.FuncAnimation(fig, animate, 
															 init_func=init, 
															 frames=l, 
															 interval=1000,
															 blit=True,
															 repeat=False)


# Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# anim.save('dreamer_two_player.mp4')
plt.show()