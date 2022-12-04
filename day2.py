
def eval_line(line):
    '''
    A: Rock, B: Paper, C: Scissors
    X: Rock, Y: Paper, Z: Scissors
    '''
    opponent_options = "ABC"
    your_options = "XYZ"
    opponents, yours = line.split(" ")
    op_index = opponent_options.find(opponents)
    your_index = your_options.find(yours)

    if op_index == your_index:
        return your_index + 1 + 3
    if (your_index - op_index) % 3 == 1:
        # Victory
        return your_index + 1 + 6
    return your_index + 1


file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/day2_input.txt"

score = 0

with open(file_path, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        score += eval_line(stripped_line)

print("Total score: ", score)