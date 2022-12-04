
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_common(line1, line2, line3):
    full_intersection = line1 & line2 & line3
    return priority.find(full_intersection.pop()) + 1


file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/venv/day3_input.txt"

total_priority = 0
with open(file_path, 'r') as file:
    for line in file:
        line1 = set(line.strip())
        line2 = set(file.readline().strip())
        line3 = set(file.readline().strip())
        total_priority += find_common(line1, line2, line3)

print(total_priority)
