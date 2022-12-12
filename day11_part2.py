import numpy as np

class Monkey:
    def __init__(self, name):
        self.name = name
        self.inspection_count = 0
        self.param = 1

    def set_items(self, items):
        self.items = items

    def set_test(self, test):
        self.test = test

    def set_true_dest(self, true_dest):
        self.true_dest = true_dest

    def set_false_dest(self, false_dest):
        self.false_dest = false_dest

    def set_operation(self, operation):
        self.operation = operation

    def throw_items(self, monkeys, lcm):
        for item in self.items:
            self.inspection_count += 1
            item = self.operation(item, self.param)
            item = item % lcm

            if item % self.test == 0:
                monkeys[self.true_dest].set_items(monkeys[self.true_dest].items + [item])
            else:
                monkeys[self.false_dest].set_items(monkeys[self.false_dest].items + [item])

        self.set_items([])

        return monkeys

file_path = "data/day11_input.txt"

with open(file_path, 'r') as file:
    monkeys = []
    for line in file:
        if line.startswith("Monkey"):
            monkeys.append(Monkey(line))
        elif line.startswith("  Starting items: "):
            str_items = line[18:].split(', ')
            items = [int(str_item) for str_item in str_items]
            print(items)
            monkeys[-1].items = items
        elif line.startswith("  Operation:"):
            equals_index = line.find('=')
            equation = line.strip()[equals_index + 2:]
            equation_segments = equation.split(' ')
            if equation_segments[2] != 'old':
                monkeys[-1].param = int(equation_segments[2])
            if equation_segments[1] == '+':
                if equation_segments[2] == 'old':
                    monkeys[-1].set_operation(lambda a, c: a + a)
                else:
                    monkeys[-1].set_operation(lambda a, c: a + c)
            elif equation_segments[1] == '*':
                if equation_segments[2] == 'old':
                    monkeys[-1].set_operation(lambda a, c: a * a)
                else:
                    monkeys[-1].set_operation(lambda a, c: a * c)

        elif line.startswith("  Test"):
            segments = line.split(" ")
            monkeys[-1].test = int(segments[-1])
        elif line.startswith("    If true:"):
            segments = line.split(" ")
            monkeys[-1].true_dest = int(segments[-1])
        elif line.startswith("    If false:"):
            segments = line.split(" ")
            monkeys[-1].false_dest = int(segments[-1])

    lcm = np.lcm.reduce([m.test for m in monkeys])
    print("Done setting monkeys")

    for i in range(10000):
        for j in range(len(monkeys)):
            monkeys = monkeys[j].throw_items(monkeys, lcm)
        print(i)

    inspection_list = [m.inspection_count for m in monkeys]

    max_inspection_list = max(inspection_list)
    inspection_list.remove(max_inspection_list)
    print("Monkey business level: ", max_inspection_list * max(inspection_list))