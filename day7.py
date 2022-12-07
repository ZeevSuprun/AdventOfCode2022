import math


class Dir:

    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.parent = parent
        self.dict_dirs = dict()
        self.dict_files = dict()

    def calculate_size(self):
        size_files = sum(self.dict_files.values())
        sub_dirs = self.dict_dirs.values()
        size_subdirs = 0
        for dir in sub_dirs:
            size_subdirs += dir.calculate_size()

        total_size = size_files + size_subdirs
        self.size = total_size
        return total_size

    def sum_sizes_less_than_threshold(self):
        sum_less_than_threshold = 0
        if self.size <= 100000:
            sum_less_than_threshold += self.size
        sub_dirs = self.dict_dirs.values()
        for dir in sub_dirs:
            sum_less_than_threshold += dir.sum_sizes_less_than_threshold()
        return sum_less_than_threshold

    def print_info(self):
        print("Dir name: ", self.name)
        print("Subdirs: ", [(item[0]) for item in self.dict_dirs.items()])
        print("Files: ", [(item[0], item[1]) for item in self.dict_files.items()])

    def get_list_all_dir_sizes(self):
        all_sizes = []
        all_sizes.append(self.size)
        sub_dirs = self.dict_dirs.values()
        for dir in sub_dirs:
            all_sizes.extend(dir.get_list_all_dir_sizes())
        return all_sizes



file_path = "data/day7_input.txt"

top_level_dir = Dir(name='/', parent=None)
current_dir = top_level_dir

with open(file_path, 'r') as file:
    # first line is to cd to top level dir.
    file.readline()

    for line in file:
        strip_line = line.strip()
        segments = strip_line.split(' ')

        if segments[0] == '$':
            if segments[1] == 'cd':
                if segments[2] == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.dict_dirs[segments[2]]

        elif segments[0] == 'dir':
            name = segments[1]
            current_dir.dict_dirs[name] = Dir(name, parent=current_dir)
        else:
            # starts with a number
            size = int(segments[0])
            name = segments[1]
            current_dir.dict_files[name] = int(size)

top_level_dir.calculate_size()
print("Part 1: ", top_level_dir.sum_sizes_less_than_threshold())

list_all_dir_sizes = top_level_dir.get_list_all_dir_sizes()
required_unused_space = 30000000
total_space_on_device = 70000000
total_unused_space = total_space_on_device - top_level_dir.size
required_additional_unused_space = required_unused_space - total_unused_space

smallest_greater_than_threshold = math.inf
for size in list_all_dir_sizes:
    if smallest_greater_than_threshold > size >= required_additional_unused_space:
        smallest_greater_than_threshold = size

print("Part 2: ", smallest_greater_than_threshold)