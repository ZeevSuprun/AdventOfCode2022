import time


def get_positions_excluded_by_sensor(sensor_pos, beacon_pos, target_y):
    beacon_dist = abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1])
    sensor_x = sensor_pos[0]
    sensor_y = sensor_pos[1]
    excluded_positions = dict()

    y_dist = abs(target_y - sensor_y)
    if y_dist <= beacon_dist:
        x_dist = beacon_dist - y_dist
        x_positions = {i for i in range(sensor_x - x_dist, sensor_x + x_dist + 1)}
        excluded_positions[target_y] = x_positions

    return excluded_positions


def merge_pos_dicts(d1, d2):
    for key in d2.keys():
        if key in d1:
            d1[key] = d1[key].union(d2[key])
        else:
            d1[key] = d2[key]
    return d1


file_path = "data/day15_test.txt"
# key = y_pos, val = set of x_positions
all_excluded_positions = dict()
all_beacons = set()
target_line = 2000000
'''
sensor_pos = (2302110,2237242)
beacon_pos = (2348729,2348729)
positions = get_positions_excluded_by_sensor(sensor_pos, beacon_pos, )
sorted_keys = list(positions.keys())
sorted_keys.sort()
for key in sorted_keys:
    print(key, ": ", positions[key])
'''

with open(file_path, 'r') as file:
    for line in file:
        print(line)
        line_segments = line.strip().split(" ")
        sensor_pos = (int(line_segments[2][2:-1]), int(line_segments[3][2:-1]))
        beacon_pos = (int(line_segments[8][2:-1]), int(line_segments[9][2:]))
        all_beacons.add(beacon_pos)

        sensor_excluded_positions = get_positions_excluded_by_sensor(sensor_pos, beacon_pos, target_line)
        all_excluded_positions = merge_pos_dicts(all_excluded_positions, sensor_excluded_positions)

    #Now need to remove real beacon positions from the list of excluded posititions
    for beacon in all_beacons:
        if beacon[1] == target_line:
            x_positions_at_beacon_y = all_excluded_positions[beacon[1]]
            if x_positions_at_beacon_y:
                all_excluded_positions[beacon[1]] = x_positions_at_beacon_y - {beacon[0]}

    print(len(all_excluded_positions[target_line]))
