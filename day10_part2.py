

def draw(screen, x, cycle_num):
    cycle_horizontal_pos = cycle_num % 40
    if cycle_horizontal_pos - 1 == x or \
       cycle_horizontal_pos - 1 == x - 1 or \
       cycle_horizontal_pos - 1 == x + 1:

        #sprite is on screen
        screen[cycle_num - 1] = '#'
    if x >= 40:
        print("I'm confused this should never happen")

    return screen


file_path = "data/day10_input.txt"

with open(file_path, 'r') as file:
    cycle_num = 0
    x = 1
    sum_signal_strengths = 0
    screen = ['.'] * 240
    for line in file:
        if line.strip() == 'noop':
            cycle_num += 1
            screen = draw(screen, x, cycle_num)
        else:
            delta = int(line.strip().split(' ')[1])
            cycle_num += 1
            screen = draw(screen, x, cycle_num)
            cycle_num += 1
            screen = draw(screen, x, cycle_num)
            x += delta

    for i in range(0, 240, 40):
        print("".join(screen[i:i+40]))




