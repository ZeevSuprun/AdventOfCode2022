def is_visible(tree_grid, row_index, col_index):
    column = [tree_grid[i][col_index] for i in range(len(tree_grid))]
    row = tree_grid[row_index][:]
    element = tree_grid[row_index][col_index]

    return element > max(column[:row_index]) or \
        element > max(column[row_index + 1:]) or \
        element > max(row[:col_index]) or \
        element > max(row[col_index + 1:])


file_path = "data/day8_input.txt"
tree_grid = []

with open(file_path, 'r') as file:
    # first line is to cd to top level dir.
    for line in file:
        row = []
        for c in line.strip():
            row.append(int(c))
        tree_grid.append(row)

num_visible = 0
# First and last row are all visible
num_visible += len(tree_grid[0]) * 2
# First and last col are all visible.
# (-2 to avoid double counting the ones in the first and last row)
num_visible += (len(tree_grid) - 2) * 2

for i in range(1, len(tree_grid) - 1):
    for j in range(1, len(tree_grid[0]) - 1):
        num_visible += is_visible(tree_grid, i, j)

print("Part 1: Num visible: ", num_visible)