from itertools import combinations

with open("input9", "r") as f:
	data = list(map(lambda i: tuple(map(lambda j: int(j), i.split(","))), f.read().split("\n")))
	
pairs = []

vertical_sides = set([])
horizontal_sides = set([])


def check_sides(sides):
	checking_vertical = False
	checking_horizontal = False
	for side1 in sides:
		# for side2 in vertical_sides | horizontal_sides:
		# 	if side2[0][0] <= side1[0][0] <= side1[1][0] <= side2[1][0] and side2[0][1] <= side1[0][1] <= side1[1][1] <= side2[1][1]:
		# 		return True
		for side2 in vertical_sides:
			if side2[0][1] <= side1[0][1] <= side1[1][1] <= side2[1][1]:
				checking_vertical = True
				break
		for side2 in horizontal_sides:
			if side2[0][0] <= side1[0][0] <= side1[1][0] <= side2[1][0]:
				checking_horizontal = True
				break
		return checking_horizontal and checking_vertical

def check_rectangle(coord1, coord2):
	sides: set = set([])
	sides.add(tuple(sorted((coord1, (coord2[0], coord1[1])), key=lambda i: i[0])))
	sides.add(tuple(sorted((coord1, (coord1[0], coord2[1])), key=lambda i: i[0])))
	sides.add(tuple(sorted((coord2, (coord1[0], coord2[1])), key=lambda i: i[0])))
	sides.add(tuple(sorted((coord2, (coord2[0], coord1[1])), key=lambda i: i[0])))
	if len(sides) < 4: return False
	elif len(sides & vertical_sides & horizontal_sides) >= 3: return True
	elif len((sides & vertical_sides) | (sides & horizontal_sides)) <= 1:
		print("asads")
		return False
	else:
		return check_sides((sides - vertical_sides) - horizontal_sides)

def get_area(item1, item2):
	x = abs(item1[0] - item2[0]) + 1
	y = abs(item1[1] - item2[1]) + 1
	return x * y

for i in range(0, len(data), 2):
	side = tuple(sorted((data[i], data[i+1]), key=lambda j: j[0]))
	horizontal_sides.add(side)
	
for i in range(1, len(data), 2):
	side = tuple(sorted((data[i], data[(i+1) % (len(data) -1)]), key=lambda j: j[0]))
	vertical_sides.add(side)


biggest = 0

for i in combinations(data, 2):
	if check_rectangle(i[0], i[1]):
		area = get_area(i[0], i[1])
		if area > biggest: biggest = area


print(biggest)