from itertools import combinations

with open("input9", "r") as f:
	data = list(map(lambda i: list(map(lambda j: int(j), i.split(","))), f.read().split("\n")))
	
pairs = []

all_sides = set([])

def check_side(side):
	for item in all_sides:
		if side[0] == side

def check_rectangle(coord1, coord2):
	sides = set([[coord1[0], coord2[0]], [coord1[1], coord2[0]], [coord1[0], coord2[1]], [coord1[1], coord2[1]]])
	if len(sides & all_sides) >= 3: return True
	elif len(sides & all_sides) <= 1: return False
	else:
		for side in sides - all_sides:
			

def get_area(item1, item2):
	x = abs(item1[0] - item2[0]) + 1
	y = abs(item1[1] - item2[1]) + 1
	return x * y

for i in	
			
for i in combinations(data, 2):
	pairs.append([get_area(i[0], i[1]), i[0], i[1]])

pairs = sorted(pairs, key=lambda i: i[0], reverse=True)

print(pairs[0][0])