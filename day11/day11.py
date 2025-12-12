with open("input11", "r") as f:
    data = f.read().split("\n")
#redoinrustsmh
data_dict = {}	
sum = 0

def search(start_key, found_dac, found_fft):
    if start_key == "out":
        if found_dac and found_fft:
            return 1
        return 0
    if start_key == "dac":
        found_dac = True
    if start_key == "fft":
        found_fft = True
    start_num = 0
    for item in data_dict[start_key]:
        if (item, found_dac, found_fft) in memo.keys():
            start_num += memo[(item, found_dac, found_fft)]
        else:
            memo[(item, found_dac, found_fft)] = search(item, found_dac, found_fft)
            start_num += memo[(item, found_dac, found_fft)]
    return start_num

memo = {}
def search_part1(start_key):
    if start_key == "out":
        return 1
    start_num = 0
    for item in data_dict[start_key]:
        if item in memo.keys():
            start_num += memo[item]
        else:
            memo[item] = search_part1(item)
            start_num += memo[item]
    return start_num

for item in data:
    line = item.split(":")
    data_dict[line[0]] = line[1].split()

#search("svr", False, False)	

print(search("svr", False, False))