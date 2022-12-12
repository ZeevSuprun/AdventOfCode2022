
import numpy as np


def get_adjacent(pos, grid):

    adjacent = []
    if pos[1] + 1 < grid.shape[1]:
        adjacent.append((pos[0], pos[1] + 1))
    if pos[1] - 1 >= 0:
        adjacent.append((pos[0], pos[1] - 1))
    if pos[0] + 1 < grid.shape[0]:
        adjacent.append((pos[0] + 1, pos[1]))
    if pos[0] - 1 >= 0:
        adjacent.append((pos[0] - 1, pos[1]))

    accessible_adjacent = []
    for adj in adjacent:
        if grid[adj] - grid[pos] <= 1:
            accessible_adjacent.append(adj)
    return accessible_adjacent


def path_find(start: tuple, goal: tuple, grid):
    traversed_positions = set()

    positions_to_traverse = [start]
    distance_from_start_grid = np.full(grid.shape, np.inf)
    distance_from_start_grid[start] = 0

    while positions_to_traverse:
        if len(traversed_positions) % 100 == 0:
            print("Iteration ", len(traversed_positions))
        current_pos = positions_to_traverse[0]
        if current_pos == goal:
            return distance_from_start_grid[current_pos]
        traversed_positions.add(current_pos)
        del positions_to_traverse[0]

        neighbours = get_adjacent(current_pos, grid)

        for neighbour in neighbours:
            if neighbour not in traversed_positions and neighbour not in positions_to_traverse:
                distance_from_start_grid[neighbour] = distance_from_start_grid[current_pos] + 1
                positions_to_traverse.append(neighbour)

file_path = "data/day12_input.txt"

line_list = []
with open(file_path, 'r') as file:
    for line in file:
        line_list.append(list(line.strip()))

letter_grid = np.array(line_list)
number_grid = np.zeros(letter_grid.shape)
start_pos = tuple()
end_pos = tuple()

for i in range(number_grid.shape[0]):
    for j in range(number_grid.shape[1]):
        if letter_grid[i, j] == 'S':
            start_pos = (i, j)
            number_grid[start_pos] = ord('a')
        elif letter_grid[i, j] == 'E':
            end_pos = (i, j)
            number_grid[end_pos] = ord('z')
        else:
            number_grid[i][j] = ord(letter_grid[i][j])

print("Size grid: ", number_grid.size)
print(path_find(start_pos, end_pos, number_grid))


# TODO find start and end pos




