
def is_full_overlap(line):
    first, second = line.split(',')
    first_start, first_end = first.split('-')
    first_range = set(range(int(first_start), int(first_end) + 1))
    second_start, second_end = second.split('-')
    second_range = set(range(int(second_start), int(second_end) + 1))

    if first_range.issubset(second_range) or second_range.issubset(first_range):
        return 1
    else:
        return 0

file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/venv/day4_input.txt"


num_full_overlaps = 0
with open(file_path, 'r') as file:
    for line in file:
        num_full_overlaps += is_full_overlap(line.strip())

print("Num full overlaps: ", num_full_overlaps)