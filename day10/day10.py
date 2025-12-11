from itertools import combinations, combinations_with_replacement


class Machine:
    def __init__(self, indicator, buttons, joltages):
        self.indicator = indicator
        self.buttons = buttons
        self.joltages = joltages
        self.init_indicator = ["."] * len(self.indicator)
        self.init_joltage = [0] * len(self.jotages)

    def check_buttons_indicators(self):
        for r in range(1, len(self.buttons) + 1):
            for i in sorted(combinations(self.buttons, r), key=lambda j : len(j)):
                indicators = self.init_indicator.copy()
                for button in i:
                    for index in button:
                        indicators[index] = "#" if indicators[index] == "." else "."
                if "".join(indicators) == self.indicator: return len(i)
        return 0

    def check_buttons_joltage(self):
        joltage_dict = dict.fromkeys(self.joltages, [])
        for r in range(1, 100):
            for i in sorted(combinations_with_replacement(self.buttons, r), key=lambda j : len(j)):
                print(i)
                joltages = self.init_joltage.copy()
                for button in i:
                    for index in button:
                        joltages[index] += 1
                if joltages == self.jotages:
                    print(i)
                    return len(i)
        return 0

    def sort_buttons(self, button, current_jolts):


with open("input10", "r") as f:
    unparsed_data = f.read().split("\n")

data: list[Machine] = []

for item in unparsed_data:
    temp_item = item.split()
    new_item = []
    new_item.append(temp_item[0][1:-1])
    buttons = []
    for i in temp_item[1:-1]:
        buttons.append(list(map(lambda j: int(j), i[1:-1].split(","))))
    new_item.append(buttons)
    new_item.append(list(map(lambda j: int(j), temp_item[-1][1:-1].split(","))))
    data.append(Machine(new_item[0], new_item[1], new_item[2]))

sum = 0
joltage_sum = 0


for i in data:
    sum += i.check_buttons_indicators()

for i in data:
    print(data.index(i))
    joltage_sum += i.check_buttons_joltage()

print(joltage_sum)

print(sum)