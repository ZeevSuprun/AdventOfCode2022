
def is_any_overlap(line):
    first, second = line.split(',')
    first_start, first_end = first.split('-')
    first_range = set(range(int(first_start), int(first_end) + 1))
    second_start, second_end = second.split('-')
    second_range = set(range(int(second_start), int(second_end) + 1))

    intersection = first_range.intersection(second_range)
    # an empty set evaluates to false
    return bool(intersection)

file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/data/day4_input.txt"


num_overlaps = 0
with open(file_path, 'r') as file:
    for line in file:
        num_overlaps += is_any_overlap(line.strip())

print("Num overlaps: ", num_overlaps)