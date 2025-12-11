with open("input11", "r") as f:
	data = f.read().split("\n")

data_dict = {}	
sum = 0

def search(start_key, found_dac, found_fft, curr_list):
	global sum
	new_list = curr_list.copy()
	for item in data_dict[start_key]:
		if item == "out":
			if found_dac and found_fft:
				print("a")
				sum += 1
			return
		else:
			if item in new_list: return
			if item == "dac":
				found_dac = True
			elif item == "fft":
				found_fft = True
			
			search(item, found_dac, found_fft)
	return

def search_part1(start_key):
	global sum
	print(sum)
	if start_key == "svr" or start_key == "you": 
		sum += len(data_dict[start_key])
	else: 
		sum += len(data_dict[start_key]) - 1
	for item in data_dict[start_key]:
		if item == "out":
			return
		else:
			search_part1(item)
	return	
	
for item in data:
	line = item.split(":")
	data_dict[line[0]] = line[1].split()

search_part1("svr")

#search("svr", False, False)	
			
print(sum)