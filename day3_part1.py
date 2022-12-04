
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_priority(rucksack):
    len_compartment = int(len(rucksack)/2)
    first_compartment = set(rucksack[:len_compartment])
    second_compartment = set(rucksack[len_compartment:])
    common_item = first_compartment.intersection(second_compartment)
    return priority.find(common_item.pop()) + 1


file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/venv/day3_input.txt"

total_priority = 0
with open(file_path, 'r') as file:
    for line in file:
        total_priority += find_priority(line.strip())

print(total_priority)
