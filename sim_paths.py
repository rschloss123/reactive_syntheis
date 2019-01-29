import json 
import random 

class Controller():

	def __init__(self, name_and_bits, file_name):
		# 'with' is context block
		# 'r' is read mode
		# 'open' is a file handle and is being stored as f 
		with open(file_name, 'r') as f :
			self.file_content = json.load(f)
		
		self.num_nodes = len(self.file_content['nodes'])
		self.name_and_bits = name_and_bits


	def simulate(self, node_init, num_steps):

		node_num = node_init

		var_list = []


		for i in range (0, num_steps):
			node = self.file_content['nodes'][node_num] 
			print " "
			print "Node #", node_num

			state_binary = node['state']
			count = 0 

			list_local = []

			for j in self.name_and_bits:


				# j is equal to a dictionary
				name = j['name']
				bits = j['bits']

				# create array slice from an array of numbers
				bin_string = state_binary[count:count+bits] # grab the section 
				bin_string = bin_string[::-1] # reverse the section
				# make an array of strings 
				bin_string = [str(str_var) for str_var in bin_string] 
				# make into string
				bin_string = ''.join(bin_string)

				val_base_10 = int(bin_string,2)

				print name+":", val_base_10
				 

				list_local.append(val_base_10)

				count+=bits 

			var_list.append(list_local)

			transition_options =  node['trans']

			not_empty = 0
			
			node_num = str(random.choice(transition_options))
			while not_empty == 0:
				next_node = self.file_content['nodes'][node_num] 
				if next_node['trans'] == []:
					node_num = str(random.choice(transition_options))
				else:
					not_empty = 1

		
		# var_list is for simulation
		return var_list





def main(): 
	
	delivery_lookup = [
		# {'name': 'work', 'bits': 1},
	
		{'name': 'wait', 'bits': 1},
		# {'name': 'refill', 'bits': 1},
		{'name': 'obstacle1', 'bits': 1},
		{'name': 'obstacle2', 'bits': 1},
		{'name': 'workload', 'bits': 5},
		{'name': 'r_state', 'bits': 2},
		{'name': 'workload_add', 'bits': 4},
		{'name': 'refill', 'bits': 1}
	]

	delivery_file = '/home/rachel/reactive_synthesis/hri_reactive_synthesis/ctrl.json'
	delivery_sim = Controller(delivery_lookup, delivery_file)
	node_init = '16'
	var_list = delivery_sim.simulate(node_init, 60)

	

if __name__ == '__main__':
	main()




	# # list of dictionaries
	# park_lookup = [
	# 	{'name': 'o_state', 'bits': 4},
	# 	{'name': 'park', 'bits': 1},
	# 	{'name': 'a_state', 'bits': 4}
	# ]

	# park_file = '/home/formal/cyberphysical_systems/hw5/prob1/ctrl.json'
	# park_sim = Controller(park_lookup, park_file)
	# node_init = '0'
	# park_sim.simulate(node_init, 50)

	# list of dictionaries
	# elevator_lookup = [
	# 	{'name': 'Call1', 'bits': 3},
	# 	# {'name': 'Call2', 'bits': 3},
	# 	{'name': 'Open', 'bits': 3},
	# 	{'name': 'Floor', 'bits': 2}
	# ]

	# elevator_lookup = [
	# 	{'name': 'Req0', 'bits': 1},
	# 	{'name': 'Req1', 'bits': 1},
	# 	{'name': 'Req2', 'bits': 1},
	# 	{'name': 'Req3', 'bits': 1},
	# 	{'name': 'Num_Req', 'bits': 2},
	# 	# {'name': 'Not_Req3', 'bits': 3},		
	# 	{'name': 'Open0', 'bits': 1},
	# 	{'name': 'Open1', 'bits': 1},
	# 	{'name': 'Open2', 'bits': 1},
	# 	{'name': 'Open3', 'bits': 1},
	# 	{'name': 'Floor', 'bits': 2}
	# ]


	# elevator_file = '/home/formal/cyberphysical_systems/hw5/prob3/elevator_deadlock.json'
	# elevator_sim = Controller(elevator_lookup, elevator_file)
	# node_init = '0'
	# elevator_sim.simulate(node_init, 2)


	# intersection_lookup = [
	# 	{'name': 'Start3', 'bits': 4},
	# 	{'name': 'Start4', 'bits': 4},
	# 	{'name': 'Start7', 'bits': 4},
	# 	{'name': 'Clear_o', 'bits': 1},
	# 	{'name': 'Init_Wait3', 'bits': 1},
	# 	{'name': 'Init_Wait4', 'bits': 1},
	# 	{'name': 'Init_Wait7', 'bits': 1},
	# 	{'name': 'C_state', 'bits': 4},
	# 	{'name': 'Clear_c', 'bits': 1}
	# ]

	# intersection_file = '/home/formal/cyberphysical_systems/hw5/prob2/ctrl_intersection.json'
	# intersection_sim = Controller(intersection_lookup, intersection_file)
	# node_init = '10'
	# intersection_sim.simulate(node_init, 10)



	
	# dreamer_lookup = [
	# 	{'name': 'h_state', 'bits': 2},
	# 	{'name': 'h_closed', 'bits': 1},
	# 	{'name': 'r_state', 'bits': 2},
	# 	{'name': 'r_closed', 'bits': 1}
	# ]

	# dreamer_file = '/home/formal/cyberphysical_systems/hw5/two_player/ctrl.json'
	# dreamer_sim = Controller(dreamer_lookup, dreamer_file)
	# node_init = '0'
	# var_list = dreamer_sim.simulate(node_init, 10)

	# print var_list