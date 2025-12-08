from traceback import print_tb

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

# def fix_range_overlaps(rang):
# 	changed = False
# 	for range in ranges:
# 		if rang[0] <= range[0] <= rang[1]:
# 			if rang[0] <= range[1] <= rang[1]:
# 				range[1] = rang[1]
# 			rang[0] = rang[0]
# 			changed = True
# 		elif rang[0] > range[0] and rang[1] < range[1]:
# 			return
# 	if not changed: ranges.append(rang)

def fix_range_overlaps(rang):
	for range in ranges:
		if range[0] <= rang[0] <= range[1]:
			if range[0] <= rang[1] <= range[1]:
				rang = [0,0]
			else:
				rang[0] = range[1] +1
		elif range[0] <= rang[1] <= range[1]:
			rang[1] = range[0] - 1
		elif rang[0] < range[0] and rang[1] > range[1]:
			fix_range_overlaps([rang[0], range[0]-1])
			fix_range_overlaps([range[1]+1,rang[1]])
			return
	ranges.append(rang)

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
	if item == "":
		break
	rang = list(map(lambda x: int(x), item.split("-")))
	fix_range_overlaps(rang)
		
for range in ranges:
	if range == [0,0]: continue
	sum += range[1] - range[0] +1
	
for range in ranges:
	for rang in ranges:
		if rang == range: print("same")
		elif range[0] < rang[0] < range[1] or range[0] < rang[1] < range[1]: print("overlap")

print(sum)

print(ranges)