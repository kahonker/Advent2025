with open("input4", "r") as f:
	data = f.read().split("\n")
	
data = list(map(lambda d: list(d), data))
check=[(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

sum = 0

def count_surround(i, j):
	surround = 0
	for item in check:
		if 0 < i+item[1] < len(data) and 0 < j+item[0] < len(data[i]):
			if data[i+item[1]][j+item[0]] == "@":
				print(data[i+item[1]][j+item[0]])
				surround += 1
	return surround

for i in range(0, len(data)):
	for j in range(0, len(data[i])):
		if data[i][j] == "@" and count_surround(i, j) < 4:
			print(count_surround(i,j))
			sum += 1
			

print(sum)
print(data)