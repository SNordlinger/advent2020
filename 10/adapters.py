def get_input(file_path):
    with open(file_path) as infile:
        lines = infile.readlines()
    return [int(line) for line in lines]


def get_jolt_differences(adapter_joltages):
    with_outlet = adapter_joltages + [0]
    sorted_joltages = sorted(with_outlet)
    device_joltage = sorted_joltages[-1] + 3
    sorted_joltages.append(device_joltage)

    differences = [0, 0, 0, 0]

    for i in range(1, len(sorted_joltages)):
        diff = sorted_joltages[i] - sorted_joltages[i-1]
        differences[diff] += 1

    return differences


def count_arrangements(adapter_joltages):
    with_outlet = adapter_joltages + [0]
    sorted_joltages = sorted(with_outlet)
    device_joltage = sorted_joltages[-1] + 3
    sorted_joltages.append(device_joltage)

    arrangement_counts = [1]
    for i in range(1, len(sorted_joltages)):
        arrangements = 0
        joltage = sorted_joltages[i]
        prev_index = i - 1
        while prev_index >= 0 and joltage - sorted_joltages[prev_index] <= 3:
            arrangements += arrangement_counts[prev_index]
            prev_index -= 1
        arrangement_counts.append(arrangements)

    return arrangement_counts[-1]


def main():
    adapter_joltages = get_input('input.txt')
    differences = get_jolt_differences(adapter_joltages)
    print(f'Part 1: {differences[1] * differences[3]}')
    print(f'Part 2: {count_arrangements(adapter_joltages)}')


if __name__ == '__main__':
    main()
