from copy import deepcopy

with open("input8", "r") as f:
	data = f.read().split("\n")
	data = list(map(lambda i: list(map(lambda j: int(j), i.split(","))), data))

circuits = []
closest = []

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
			
print(closest)