from sympy.ntheory import factorint
import numpy as np


class Monkey:
    def __init__(self, name):
        self.name = name
        self.inspection_count = 0
        self.param = 1
        self.operation_type = '*'

    def set_items(self, items):
        # items is a list of dictionaries
        self.items = items

    def set_test(self, test):
        self.test = test

    def set_true_dest(self, true_dest):
        self.true_dest = true_dest

    def set_false_dest(self, false_dest):
        self.false_dest = false_dest

    def throw_items(self, monkeys):
        for factorized_item in self.items:
            self.inspection_count += 1

            if self.operation_type == '*':
                if self.param in factorized_item:
                    #parameter is already a factor
                    factorized_item[self.param] += 1
                else:
                    factorized_item[self.param] = 1
            elif self.operation_type == '^2':
                for key in factorized_item:
                    factorized_item[key] *= 2
            elif self.operation_type == '+':
                item = np.prod([key ** factorized_item[key] for key in factorized_item.keys()])
                item += self.param
                factorized_item = factorint(item)
            else:
                print("error improper operation parsed ")


            if self.test in factorized_item:
                monkeys[self.true_dest].set_items(monkeys[self.true_dest].items + [factorized_item])
            else:
                monkeys[self.false_dest].set_items(monkeys[self.false_dest].items + [factorized_item])

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
            factorized_items = []
            for item in items:
                factorized_items.append(factorint(item))

            monkeys[-1].items = factorized_items
        elif line.startswith("  Operation:"):
            equals_index = line.find('=')
            equation = line.strip()[equals_index + 2:]
            equation_segments = equation.split(' ')
            if equation_segments[2] != 'old':
                monkeys[-1].param = int(equation_segments[2])
                monkeys[-1].operation_type = equation_segments[1]
            else:
                monkeys[-1].operation_type = '^2'

        elif line.startswith("  Test"):
            segments = line.split(" ")
            monkeys[-1].test = int(segments[-1])
        elif line.startswith("    If true:"):
            segments = line.split(" ")
            monkeys[-1].true_dest = int(segments[-1])
        elif line.startswith("    If false:"):
            segments = line.split(" ")
            monkeys[-1].false_dest = int(segments[-1])


    print("Done setting monkeys")

    for i in range(10000):
        for j in range(len(monkeys)):
            monkeys = monkeys[j].throw_items(monkeys)
        print(i)

    inspection_list = []
    for monkey in monkeys:
        print(monkey.name, ": ", monkey.items)
        inspection_list.append(monkey.inspection_count)

    max_inspection_list = max(inspection_list)
    inspection_list.remove(max_inspection_list)
    print("Monkey business level: ", max_inspection_list * max(inspection_list))