import decimal

with open("input6", "r") as f:
    data = f.read().split("\n")

data = data


for i in range(0, len(data[0])-1):
    for j in range(0, len(data)):
        if data[0][i] != " " or data[1][i] != " " or data[2][i] != " " or data[3][i] != " ":
            if data[j][i] == " ": data[j] = data[j][:i] + "." + data[j][i+1:]


split_data = list(map(lambda i: i.split(), data))
total_sum = 0

def get_stange_num_list(list):
    listed = []
    for i in range(0, len(max(list, key=len))):
        new_num = ""
        for j in range(len(list)-1):
            new_num += list[j][i]
        new_num = new_num.replace(".", "")
        listed.append(int(new_num))
    listed.append(list[-1].replace(".", ""))
    return listed

for i in range(0,len(split_data[0])):
    listed = []
    evaluation = 0
    for j in range(0, len(split_data)):
        if split_data[j][i].isdigit(): listed.append(split_data[j][i])
        else: listed.append(split_data[j][i])

    listed = get_stange_num_list(listed)
    print(listed)
    for j in range(0, len(listed)-1):
        if listed[-1] == "+":
            evaluation += listed[j]
        if listed[-1] == "*":
            if j == 0:
                evaluation = 1
            evaluation *= listed[j]
    total_sum += evaluation
#

print(total_sum)