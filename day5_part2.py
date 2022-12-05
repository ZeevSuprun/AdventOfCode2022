
def execute_moves(list_of_stacks, instruction):
    split_instruction = instruction.strip().split(' ')
    print(split_instruction)
    num_pops = int(split_instruction[1])
    source_stack_index = int(split_instruction[3]) - 1
    dest_stack_index = int(split_instruction[5]) - 1

    moved = list_of_stacks[source_stack_index][-num_pops:]
    del(list_of_stacks[source_stack_index][-num_pops:])
    list_of_stacks[dest_stack_index].extend(moved)


file_path = "data/day5_input.txt"

initial_conditions = []
list_of_stacks = []

with open(file_path, 'r') as file:
    # First extract the initial list of stacks
    for line in file:
        if line.startswith(' 1'):
            num_stacks = int(line.strip()[-1])
            print(num_stacks)
            list_of_stacks = [[] for i in range(num_stacks)]
            break

        initial_conditions.append(line)

    for line in initial_conditions:
        # for a list of 1 to 9, the indices you want are:
        # 1, 5, 9, 13
        important_indices = [i for i in range(1, len(line), 4)]
        for count, i in enumerate(important_indices):
            if line[i] != ' ':
                list_of_stacks[count].insert(0, line[i])

    # initial list of stacks is no populated
    for instruction in file:
        if instruction.startswith(('move')):
            execute_moves(list_of_stacks, instruction.strip())

output_string = ""
for stack in list_of_stacks:
    output_string += stack.pop()

print(output_string)

