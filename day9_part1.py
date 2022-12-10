import numpy as np


def update_tail_pos(tail_pos, head_pos):
    if tail_pos[0] == head_pos[0]:
        # same row
        tail_pos[1] += 1 * np.sign(head_pos[1] - tail_pos[1])
    elif tail_pos[1] == head_pos[1]:
        # same col
        tail_pos[0] += 1 * np.sign(head_pos[0] - tail_pos[0])
    else:
        # need to move diagonally
        tail_pos[1] += 1 * np.sign(head_pos[1] - tail_pos[1])
        tail_pos[0] += 1 * np.sign(head_pos[0] - tail_pos[0])

    return tail_pos


file_path = "data/day9_input.txt"

tail_positions = set()
tail_pos = np.array([0,0])
head_pos = np.array([0,0])
tail_positions.add(tuple(tail_pos))


with open(file_path, 'r') as file:
    for line in file:
        split_line = line.strip().split(' ')
        direction = split_line[0]
        dist = int(split_line[1])

        for i in range(dist):
            # Update head pos:
            if direction == 'R':
                head_pos[1] += 1
            elif direction == 'L':
                head_pos[1] -= 1
            elif direction == 'U':
                head_pos[0] += 1
            elif direction == 'D':
                head_pos[0] -= 1

            # Check adjacency.
            if np.linalg.norm(head_pos - tail_pos) >= 2:
                # Not adjacent, update tail position
                tail_pos = update_tail_pos(tail_pos, head_pos)
                tail_positions.add(tuple(tail_pos))

    print("Num unique postions visited: ", len(tail_positions))









