import copy

with open("input4", "r") as f:
	data = f.read().split("\n")
	
data = list(map(lambda d: list(d), data))
check=[(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

sum = 0

coordinates = []

new_data = [[]]



def count_surround(i, j, data):
	surround = 0
	for item in check:
		coordinate = (i+item[1], j+item[0])
		if not (0 > coordinate[0] or 0 > coordinate[1] or coordinate[0] > len(data)-1 or coordinate[1] > len(data[i]) -1):
			if data[coordinate[0]][coordinate[1]] == "@":
				surround += 1

	return surround

def pretty_print(data):
	for line in data:
		print("".join(line))

def find_rolls(data):
	sum = 0
	for i in range(0, len(data)):
		for j in range(0, len(data[i])):
			if data[i][j] == "@" and count_surround(i, j, data) < 4:
				new_data[i][j] = "x"
				sum += 1
	return sum

count = 1
overall = 0

while count > 0:
	new_data = copy.deepcopy(data)
	print(new_data)
	count = find_rolls(new_data)
	overall += count
	data = new_data


print(data)

print(overall)