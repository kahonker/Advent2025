from copy import deepcopy

with open("input8", "r") as f:
	data = f.read().split("\n")
	data = list(map(lambda i: list(map(lambda j: int(j), i.split(","))), data))

circuits = []
closest = []

def check_in_circuits(check):
	for circuit in circuits:
		if check in circuit:
			return True
	return False
	
def add_circuit(item1, item2):
	if check_in_circuits(item2):
		for i in range(len(circuits)):
			if item2 in circuits[i]:
				circuits[i].append(item1)
				return
	else:
		circuits.append([item1, item2])

for item in data:
	smallest_dist = 0
	new_data = deepcopy(data)
	new_data.remove(item)
	for item2 in new_data:
		x_distance = abs(item[0] - item2[0])
		y_distance = abs(item[1] - item2[1])
		z_distance = abs(item[2] - item2[2])
		distance = (x_distance ** 2 + y_distance **2 + z_distance ** 2) ** .5
		if distance < smallest_dist or smallest_dist == 0:
			smallest_dist = distance
			closest = [item, item2]
		add_circuit(item, item2)

circuits = sorted()			
									
print(closest)