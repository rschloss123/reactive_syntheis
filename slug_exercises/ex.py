import json
import random
import time
from environment import Simulation
from time import sleep

def get_o_state(node):
    return node['state'][3]*(2**3) + node['state'][2]*(2**2) + node['state'][1]*(2**1)\
           + node['state'][0]*(2**0)

def get_a_state(node):
    print node
    return node['state'][7]*2**3 + node['state'][6]*2**2 + node['state'][5]*2**1\
           + node['state'][4]*2**0


def xy_to_state(arr):
    if arr[0] == 0 and arr[1] == 0:
        return 12
    elif arr[0] == 0 and arr[1] == 1:
        return 8
    elif arr[0] == 0 and arr[1] == 2:
        return 4
    elif arr[0] == 0 and arr[1] == 3:
        return 0
    elif arr[0] == 1 and arr[1] == 0:
        return 13
    elif arr[0] == 1 and arr[1] == 1:
        return 9
    elif arr[0] == 1 and arr[1] == 2:
        return 5
    elif arr[0] == 1 and arr[1] == 3:
        return 1
    elif arr[0] == 2 and arr[1] == 0:
        return 14
    elif arr[0] == 2 and arr[1] == 1:
        return 10
    elif arr[0] == 2 and arr[1] == 2:
        return 6
    elif arr[0] == 2 and arr[1] == 3:
        return 2
    elif arr[0] == 3 and arr[1] == 0:
        return 15
    elif arr[0] == 3 and arr[1] == 1:
        return 11
    elif arr[0] == 3 and arr[1] == 2:
        return 7
    elif arr[0] == 3 and arr[1] == 3:
        return 3
    else:
        raise ValueError('Unrecognizable argument: ' + str(arr))


def state_to_xy(state):
    if state == 12:
        return (0, 0)
    elif state == 8:
        return (0, 1)
    elif state == 4:
        return (0, 2)
    elif state == 0:
        return (0, 3)
    elif state == 13:
        return (1, 0)
    elif state == 9:
        return (1, 1)
    elif state == 5:
        return (1, 2)
    elif state == 1:
        return (1, 3)
    elif state == 14:
        return (2, 0)
    elif state == 10:
        return (2, 1)
    elif state == 6:
        return (2, 2)
    elif state == 2:
        return (2, 3)
    elif state == 15:
        return (3, 0)
    elif state == 11:
        return (3, 1)
    elif state == 7:
        return (3, 2)
    elif state == 3:
        return (3, 3)
    else:
        raise ValueError('Unrecognizable argument: ' + str(state))


def get_action(cur_pos, next_pos):
    if next_pos[0] - cur_pos[0] == 1 and next_pos[1] - cur_pos[1] == 0:
        return "east"
    elif next_pos[0] - cur_pos[0] == -1 and next_pos[1] - cur_pos[1] == 0:
        return "west"
    elif next_pos[1] - cur_pos[1] == 1 and next_pos[0] - cur_pos[0] == 0:
        return "south"
    elif next_pos[1] - cur_pos[1] == -1 and next_pos[0] - cur_pos[0] == 0:
        return "north"
    elif next_pos[1] - cur_pos[1] == 0 and next_pos[0] - cur_pos[0] == 0:
        return "stay"
    else:
        raise ValueError('Invalid input: cur_pos ' + str(cur_pos) + ', next_pos ' + str(next_pos))


with open('ctrl.json') as f:
    data = json.load(f)

nodes = data['nodes']

sim = Simulation('ex.config')
sim.draw()
cur_state = sim.get_state()
a_state = xy_to_state(cur_state['agents'][0])
o_state = xy_to_state(cur_state['moving_obstacles'][0])
current_node = nodes['130']


while True:
    trans = current_node['trans']
    index = str(random.choice(trans))
    current_node = nodes[index]
    next_o_state = get_o_state(current_node)
    next_a_state = get_a_state(current_node)
    a_state_pos = state_to_xy(a_state)
    o_state_pos = state_to_xy(o_state)
    next_a_state_pos = state_to_xy(next_a_state)
    next_o_state_pos = state_to_xy(next_o_state)
    a_action = get_action(a_state_pos, next_a_state_pos)
    o_action = get_action(o_state_pos, next_o_state_pos)
    sim.move_agent(0, a_action)
    sim.move_obstacle(0, o_action)
    a_state = next_a_state
    o_state = next_o_state
    sim.draw()
    sleep(1)
