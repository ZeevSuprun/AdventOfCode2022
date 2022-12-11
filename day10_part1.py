

def check_signal_strength(cycle_num, x):
    if (cycle_num - 20) % 40 == 0:
        print(f"Cycle num: {cycle_num}, X: {x}, strength: {x*cycle_num}")
        return x * cycle_num
    return 0


file_path = "data/day10_input.txt"

with open(file_path, 'r') as file:
    cycle_num = 0
    x = 1
    sum_signal_strengths = 0
    for line in file:
        if line.strip() == 'noop':
            cycle_num += 1
            sum_signal_strengths += check_signal_strength(cycle_num, x)
        else:
            delta = int(line.strip().split(' ')[1])
            cycle_num += 1
            sum_signal_strengths += check_signal_strength(cycle_num, x)
            cycle_num += 1
            sum_signal_strengths += check_signal_strength(cycle_num, x)
            x += delta

    print("Sum signal strength: ", sum_signal_strengths)




