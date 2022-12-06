
file_path = "data/day6_input.txt"

with open(file_path, 'r') as file:
    buffer = file.readline()
    last_four = []
    for index, character in enumerate(buffer):
        last_four.append(character)
        # change 3 to 13 for part 2
        if index >= 3:
            # change 4 to 14 for part 2
            if len(set(last_four)) == 4:
                print("First marker at index: ", index + 1)
                break
            del last_four[0]