
def eval_line(line):
    '''
    A: Rock, B: Paper, C: Scissors
    X: Lose, Y: Draw, Z: Win
    '''
    opponent_options = "ABC"
    your_options = "ABC"
    opponents, yours = line.split(" ")
    op_index = opponent_options.find(opponents)

    if yours == 'Z':
        # Victory
        your_index = (op_index + 1) % 3
        return your_index + 1 + 6
    if yours == 'Y':
        # draw
        your_index = op_index
        return your_index + 1 + 3
    if yours == 'X':
        # Lose
        your_index = (op_index - 1) % 3
        return your_index + 1

file_path = "/Users/zeev/PycharmProjects/AdventOfCode2022/day2_input.txt"

score = 0

with open(file_path, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        score += eval_line(stripped_line)

print("Total score: ", score)