def get_score(tree_grid, row_index, col_index):
    column = [tree_grid[i][col_index] for i in range(len(tree_grid))]
    row = tree_grid[row_index][:]
    element = tree_grid[row_index][col_index]

    lists_to_check = []
    lists_to_check.append(column[:row_index])
    lists_to_check[-1].reverse() # looking backwards here
    lists_to_check.append(column[row_index + 1:])
    lists_to_check.append(row[:col_index])
    lists_to_check[-1].reverse()
    lists_to_check.append(row[col_index + 1:])

    score = 1

    for list_to_check in lists_to_check:
        view_for_line = len(list_to_check)
        for i, el in enumerate(list_to_check):
            # Assume fully unobstructed view
            if el >= element:
                # update the assumption
                view_for_line = i + 1
                break
        score *= view_for_line

    return score

file_path = "data/day8_input.txt"
tree_grid = []

with open(file_path, 'r') as file:
    # first line is to cd to top level dir.
    for line in file:
        row = []
        for c in line.strip():
            row.append(int(c))
        tree_grid.append(row)

highest_score = 0

for i in range(len(tree_grid)):
    for j in range(len(tree_grid[0])):
        score = get_score(tree_grid, i, j)
        if score > highest_score:
            highest_score = score

print("Highest score: ", highest_score)