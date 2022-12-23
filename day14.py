
def add_sand(occupied, start_x):
    num_particles = 0
    while True:
        current_x = start_x
        current_y = 0
        # for each sand particle
        num_particles += 1
        while True:
            # slide until it stops
            # check underneath
            if current_y + 1 in occupied and current_x in occupied[current_y + 1]:
                # check down and left
                if current_x - 1 not in occupied[current_y + 1]:
                    current_x -= 1
                    current_y += 1
                elif current_x + 1 not in occupied[current_y + 1]:
                    current_x += 1
                    current_y += 1
                else:
                    #stop sliding
                    if current_y == 0:
                        # end condition to part 2, sand hole is plugged
                        return num_particles
                    #print(f"particle {num_particles} has stopped at {current_x}, {current_y}")
                    if current_y in occupied:
                        occupied[current_y].add(current_x)
                    else:
                        occupied[current_y] = {current_x}
                    break
            else:
                # drop until there's something underneath
                y_values = list(occupied.keys())
                y_values.sort()
                has_stopped = False

                for y_val in y_values:
                    if y_val > current_y and current_x in occupied[y_val]:
                        # have hit the bottom
                        current_y = y_val - 1
                        has_stopped = True
                        break
                if not has_stopped:
                    print("Sand falling infinitely")
                    # Sand falls infinitely from this point
                    return num_particles


file_path = "data/day14_test.txt"
# key = y position, val = x positions set
occupied_grid = dict()

with open(file_path, 'r') as file:
    for line in file:
        segments = line.strip().split("->")
        #print(segments)
        for i in range(len(segments[:-1])):
            start_x = int(segments[i].split(",")[0])
            start_y = int(segments[i].split(",")[1])

            end_x = int(segments[i+1].split(",")[0])
            end_y = int(segments[i+1].split(",")[1])

            if start_x == end_x:
                first = min(start_y, end_y)
                second = max(start_y, end_y)
                for j in range(first, second + 1):
                    if j in occupied_grid:
                        occupied_grid[j].add(start_x)
                    else:
                        occupied_grid[j] = {start_x}
            else:
                first = min(start_x, end_x)
                second = max(start_x, end_x)
                new_elements = {j for j in range(first, second + 1)}
                if start_y in occupied_grid:
                    occupied_grid[start_y].update(new_elements)
                else:
                    occupied_grid[start_y] = new_elements

is_part_2 = True
if is_part_2:
    max_y = max(occupied_grid.keys())
    floor_level = max_y + 2
    occupied_grid[floor_level] = {i for i in range(-1000, 1000)}

#print("Part 1: ", add_sand(occupied_grid, 500) - 1)
print("Part 2: ", add_sand(occupied_grid, 500))



