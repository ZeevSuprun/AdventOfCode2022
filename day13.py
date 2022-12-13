from ast import literal_eval

def compare_lists(left, right):
    '''
    return codes:
        1: list is in order
        -1: list is out of order
         0: no decision made
    '''
    zipped_list = zip(left, right)

    for pair in zipped_list:
        l = pair[0]
        r = pair[1]
        #print(f"Comparing {l} to {r}")
        if type(l) == type(r) and type(l) == type(1):
            # both integers
            # todo figure out this base case
            if l < r:
                return 1
            if l > r:
                return -1
        elif type(l) == type(r):
            # both are lists
            result = compare_lists(l, r)
            if result != 0:
                return result
        else:
            # one is a list nd one is not
            if type(l) == type(1):
                l = [l]
            else:
                r = [r]
            result = compare_lists(l, r)
            if result != 0:
                return result
    # both lists are out of items
    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0

def part1():
    file_path = "data/day13_test.txt"

    with open(file_path, 'r') as file:
        index = 0
        sum_correct_indices = 0
        while True:
            index += 1
            left = literal_eval(file.readline().strip())
            right = literal_eval(file.readline().strip())
            result = compare_lists(left, right)
            if result == 1:
                sum_correct_indices += index

            # Read the line of whitespace
            if len(file.readline()) == 0:
                break

        print("sum correct indices: ", sum_correct_indices)

################################################################################
################################################################################
################################################################################


def merge(packets_a, packets_b):
    result = []
    while packets_a and packets_b:
        comparison = compare_lists(packets_a[0], packets_b[0])
        if comparison == 1:
            result.append(packets_a[0])
            packets_a = packets_a[1:]
        else:
            result.append(packets_b[0])
            packets_b = packets_b[1:]

    for a in packets_a:
        result.append(a)
    for b in packets_b:
        result.append(b)

    return result


def merge_sort(list_packets):
    if len(list_packets) <= 1:
        return list_packets
    half_len = int(len(list_packets) / 2)
    packets_a = list_packets[:half_len]
    packets_b = list_packets[half_len:]
    sorted_a = merge_sort(packets_a)
    sorted_b = merge_sort(packets_b)

    return merge(sorted_a, sorted_b)


def part2():
    file_path = "data/day13_test.txt"
    list_all_packets = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                list_all_packets.append(literal_eval(line.strip()))
    key1 = [[2]]
    key2 = [[6]]
    list_all_packets.append(key1)
    list_all_packets.append(key2)

    sorted_packets = merge_sort(list_all_packets)
    key1_ind = 0
    key2_ind = 0
    for i, packet in enumerate(sorted_packets):
        if packet == key1:
            key1_ind = i + 1
        elif packet == key2:
            key2_ind = i + 1
    print(key1_ind * key2_ind)



part2()