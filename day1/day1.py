with open("input1.txt", "r") as f:
    input = f.read().split("\n")

starting_pos = 50
largest_pos = 99
smallest_pos = 0
counter = 0


def go_left(amount):
    global starting_pos
    global counter
    while amount > 0:
        starting_pos -= 1;
        if starting_pos == -1:
            starting_pos = 99

        if starting_pos == 0:
            counter += 1

        amount -= 1


def go_right(amount):
    global starting_pos
    global counter
    while amount > 0:
        starting_pos += 1
        if starting_pos == 100:
            starting_pos = 0

        if starting_pos == 0:
            counter += 1

        amount -= 1

for operation in input:
    print(starting_pos)

    if operation[0:1] == "L":
        go_left(int(operation[1:]))
    else:
        go_right(int(operation[1:]))


    # if starting_pos == 0:
    #     counter += 1


print(counter)
