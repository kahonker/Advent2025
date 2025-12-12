with open("input12", "r") as f:
    data = f.read().split("\n\n")

boxes = []
trees = []

for i in data:
    if data.index(i) < len(data) - 1:
        boxes.append(list(map(lambda b: list(b), i[3:].split("\n"))))
    else:
        all_trees = i.split("\n")
        for tree in all_trees:
            trees.append((list(map(lambda l: int(l), tree.split(":")[0].split("x"))), list(map(lambda l: int(l), tree.split(":")[1].split()))))

print(trees)
count = 0

for i in trees:
    area1 = i[0][0] * i[0][1]
    print(area1)
    area2 = 0
    for j in i[1]:
        area2 += j * 7
    print(area2)
    if area2 <= area1: count += 1


print("count: ", count)
print(trees)
