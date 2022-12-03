
#file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/test_input.txt"
file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/day1_input"

current_total = 0
top_three = set()

with open(file_path, 'r') as file:
    for line in file:
        if line.isspace():
            if len(top_three) < 3:
                top_three.add(current_total)
            elif current_total > min(top_three):
                top_three.discard(min(top_three))
                top_three.add(current_total)
            current_total = 0
        else:
            current_total += int(line)

print("Top three total: ", sum(top_three))