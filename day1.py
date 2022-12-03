
file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/day1_input"

largest_total = 0
current_total = 0

with open(file_path, 'r') as file:
    for line in file:
        if line.isspace() or not line:
            if current_total > largest_total:
                largest_total = current_total
            current_total = 0
        else:
            current_total += int(line)

print("Largest total: ", largest_total)