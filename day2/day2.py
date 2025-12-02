import re

with open("input2", "r") as f:
	data = f.read().split(",")
	
sum = 0
	
for id_range in data:
	ids = id_range.split("-")
	for i in range(int(ids[0]), int(ids[1])+1):
		if re.fullmatch(r"^([0-9]+)\1+$", str(i)):
			sum += i	



print(sum)