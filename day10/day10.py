import time
from itertools import combinations


class Machine:
    def __init__(self, indicator, buttons, joltages):
        self.indicator = indicator
        self.buttons = buttons
        self.joltages = joltages
        self.init_indicator = ["."] * len(self.indicator)
        self.init_joltage = [0] * len(self.joltages)

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
        joltage_dict = dict.fromkeys(range(len(self.joltages)), [])
        num_button_pressed = 0
        while self.init_joltage != self.joltages:
            buttons_list = sorted(self.buttons, key=lambda button: self.sort_buttons(button, self.init_joltage))
            print(buttons_list)
            print(self.init_joltage)
            time.sleep(0.5)
            chosen_button = buttons_list[0]
            num_button_pressed += 1
            for i in chosen_button:
                self.init_joltage[i] += 1
                joltage_dict[i].append(chosen_button)
            listed = self.check_list_greater(self.init_joltage, self.joltages)
            if listed:
                button = joltage_dict[listed[0]][0]
                for i in button:
                    joltage_dict[i].remove(button)
                    self.init_joltage[i] -= 1
                num_button_pressed -= 1
        return num_button_pressed

    def check_list_greater(self, jolts_to_check, needed_jolts):
        return_list = []
        for i in range(len(jolts_to_check)):
            if jolts_to_check[i] > needed_jolts[i]:
                return_list.append(i)
        return return_list

    def sort_buttons(self, button, current_jolts):
        joltage_diff = [a - b for a, b in zip(self.joltages, current_jolts)]
        affecting = 0
        smallest_affecting = 0
        for index in button:
            jolts_at_index = joltage_diff[index]
            if joltage_diff[index] > 0: affecting += 1
            if self.init_joltage[index] < smallest_affecting or smallest_affecting == 0: smallest_affecting = self.init_joltage[index]
        return -affecting, len(button), -smallest_affecting

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
    print(i)
    joltage_sum += i.check_buttons_joltage()

print(joltage_sum)

print(sum)