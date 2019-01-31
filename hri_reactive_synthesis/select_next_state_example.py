import random
import json
import os 

path_location = os.path.dirname(os.path.realpath(__file__))
node_file = os.path.join(path_location, 'node_dictionary.json')
transition_file = os.path.join(path_location, 'transition_dictionary.json')

with open(node_file, 'r') as f:
    nodes_dict = json.load(f)

with open(transition_file, 'r') as f:
    transitions_dict = json.load(f)
    

check_1428 =  {'obstacle2': 0, 'workload': 18, 'obstacle3': 0, 'complete_work_with_robot': 1, 'arriving_at_0': 0, 'r_state': 0, 'workload_add': 0, 'complete_work_at_workstation': 1, 'complete_dropoff_tries': 1, 'next_state_is_workstation': 0, 'complete_dropoff_success': 1, 'wait': 0}

for key, node in nodes_dict.items():
	if nodes_dict[key] == check_1428:
		print key 
		transition_options = transitions_dict[key]
		print transition_options
		print (random.choice(transition_options))
		print nodes_dict[key]['r_state']