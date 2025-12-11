from copy import deepcopy
import heapq
from itertools import combinations

with open("input8", "r") as f:
    data = f.read().split("\n")
    data = list(map(lambda i: tuple(map(lambda j: int(j), i.split(","))), data))

circuits = []
closest = []
pairs = []

def check_in_circuits(check):
    for circuit in circuits:
        if check in circuit:
            return circuit
    return None

def merge_circuits(circuit1, circuit2):
    circuits.remove(circuit2)
    circuit1.extend(circuit2)


def add_circuit(item1, item2):
    item1_in_circuits = check_in_circuits(item1)
    item2_in_circuits = check_in_circuits(item2)
    if item1_in_circuits and item2_in_circuits:
        if item1_in_circuits is item2_in_circuits:
            return
        merge_circuits(item1_in_circuits, item2_in_circuits)
    elif item2_in_circuits:
        item2_in_circuits.append(item1)
    elif item1_in_circuits:
        item1_in_circuits.append(item2)
    else:
        circuits.append([item1, item2])


def get_distance(item1, item2):
    x_distance = item1[0] - item2[0]
    y_distance = item1[1] - item2[1]
    z_distance = item1[2] - item2[2]
    distance = (x_distance ** 2 + y_distance ** 2 + z_distance ** 2) ** .5
    return distance

def check_complete():
    for item in data:
        if check_in_circuits(item) is None: return False
    return True

for item in combinations(data, 2):
    heapq.heappush(pairs, (get_distance(item[0], item[1]), item[0], item[1]))

count = 1000
condition = False
while not check_complete():
    smallest = heapq.heappop(pairs)
    add_circuit(smallest[1], smallest[2])
    mult = smallest[1][0] * smallest[2][0]

print(mult)

circuits = sorted(circuits, key = lambda i: len(i), reverse=True)
print(circuits[0], circuits[1], circuits[2])
print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))