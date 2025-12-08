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

def sort_coordinates(coordinate, list_coordinate):
	x_distance = coordinate[0] - list_coordinate[0]
	y_distance = coordinate[1] - list_coordinate[1]
	z_distance = coordinate[2] - list_coordinate[2]
	distance = (x_distance ** 2 + y_distance ** 2 + z_distance ** 2) ** .5
	return distance

for item in data:
	smallest_dist = 0
	new_data = deepcopy(data)
	new_data.remove(item)
	item2 = sorted(new_data, key=lambda i: sort_coordinates(item, new_data[new_data.index(i)]))[0]
	add_circuit(item, item2)

circuits = sorted(circuits, key = lambda i: len(i), reverse=True)
print(circuits[0], circuits[1], circuits[2])
print(len(circuits[0]), len(circuits[1]), len(circuits[2]))