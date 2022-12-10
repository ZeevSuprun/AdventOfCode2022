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


def num_unique_tail_positions(num_knots):
    file_path = "data/day9_input.txt"

    tail_positions = set()
    knot_list = [np.array([0,0]) for i in range(num_knots)]
    tail_positions.add(tuple(knot_list[-1]))

    with open(file_path, 'r') as file:
        for line in file:
            split_line = line.strip().split(' ')
            direction = split_line[0]
            dist = int(split_line[1])

            for i in range(dist):
                # Update head pos:
                if direction == 'R':
                    knot_list[0][1] += 1
                elif direction == 'L':
                    knot_list[0][1] -= 1
                elif direction == 'U':
                    knot_list[0][0] += 1
                elif direction == 'D':
                    knot_list[0][0] -= 1

                # For every knot behind the head, check adjacency and update:
                for i in range(1, len(knot_list)):

                    if np.linalg.norm(knot_list[i - 1] - knot_list[i]) >= 2:
                        # Not adjacent, update next knot position
                        knot_list[i] = update_tail_pos(knot_list[i], knot_list[i-1])

                tail_positions.add(tuple(knot_list[-1]))

        print("Num unique postions visited: ", len(tail_positions))


# Part 1:
# num_unique_tail_positions(2)
# Part 2:
num_unique_tail_positions(10)






