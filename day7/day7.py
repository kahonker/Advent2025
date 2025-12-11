from collections import defaultdict
from math import comb

with open("input7", "r") as f:
    new_data = [list(line) for line in f.read().split("\n")]

data: list[str] = []

for line in new_data:
        if set(line) != {"."}:
            data.append(line)

new_data = []
indexes  = {}

list_splitters = []

def find_timelines(index_y, index_x):
    global sum
    for i in range(index_y, len(data)):
        if data[i][index_x] == ".": data[i][index_x] = "|"
        for item in data:
            print("".join(item))
        if data[i][index_x] == "^":
            for k in [-1, 1]:
                find_timelines(i, index_x + k)
            sum += 1
            return


for i in range(0, len(data)):
    if "S" in data[i]:
        indexes[data[i].index("S")] = 1
    next_row = defaultdict(int)
    for col, count in indexes.items():
        print(data[i][col])
        if data[i][col] == "^":
            next_row[col - 1] += count
            next_row[col + 1] += count
        else:
            next_row[col] += count
    indexes = next_row

for item in data:
    print("".join(item))

print(sum(indexes.values()))