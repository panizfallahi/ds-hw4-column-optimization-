def main():
    with open("input.txt", "r") as file_in:
        count = int(file_in.readline().strip())
        block_list = []
        for index in range(count):
            dimensions = list(map(int, file_in.readline().split()))
            dimensions.sort(reverse=True)
            length, width, height = dimensions
            block_list.append((length, width, height, index + 1))

    max_diameter = 0
    selected_blocks = []

    base_dict = {}

    for length, width, height, block_id in block_list:
        if height > max_diameter:
            max_diameter = height
            selected_blocks = [block_id]

        base_key = (length, width)
        if base_key not in base_dict:
            base_dict[base_key] = []
        base_dict[base_key].append((height, block_id))

    for (length, width), height_list in base_dict.items():
        if len(height_list) < 2:
            continue

        height_list.sort(reverse=True)

        top_height, first_id = height_list[0]
        second_height, second_id = height_list[1]

        total_height = top_height + second_height
        current_diameter = min(width, total_height)

        if current_diameter > max_diameter:
            max_diameter = current_diameter
            selected_blocks = sorted([first_id, second_id])

    with open("output.txt", "w") as file_out:
        file_out.write(str(len(selected_blocks)) + "\n")
        file_out.write(" ".join(map(str, selected_blocks)) + "\n")
        file_out.write(str(max_diameter) + "\n")


if __name__ == "__main__":
    main()
