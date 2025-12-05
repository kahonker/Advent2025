with open("input5", "r") as f:
	data = f.read().split("\n")

ranges = []
ids= []

def check_ranges(id):
	fresh = False
	for range in ranges:
		if range[0] <= id <= range[1]:
			fresh = True
	return fresh
	
check_rang = True
sum = 0

for item in data:
	if item == "":
		check_rang = False
	elif check_rang:
		rang = list(map(lambda x: int(x), item.split("-")))
		ranges.append(rang)
	else:
		if check_ranges(int(item)):
			sum += 1

ranges.clear()
sum = 0

for item in data:
	print((item))
	if item == "":
		break
	rang = list(map(lambda x: int(x), item.split("-")))
	for range in ranges:
		if range[0] <= rang[0] <= range[1]:
			if range[0] <= rang[1] <= range[1]:
				rang = [0,0]
			else:
				rang[0] = range[1] +1
		if range[0] 

print(sum)

print(len(ids))
	