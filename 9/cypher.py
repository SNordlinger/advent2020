def get_input(file_path):
    with open(file_path) as infile:
        lines = infile.readlines()
    return [int(line) for line in lines]


def has_sum(search_list, target_sum):
    for i, first_num in enumerate(search_list[:-1]):
        if first_num >= target_sum:
            continue
        remaining = target_sum - first_num
        if remaining in search_list[i+1:]:
            return True

    return False


def find_invlid_num(preamble, numbers):
    search_list = preamble.copy()
    for n in numbers:
        if not has_sum(search_list, n):
            return n
        else:
            search_list.pop(0)
            search_list.append(n)

    raise Exception('Cannot find invalid number')


def find_contiguous_sum(numbers, target_sum):
    sum_start = 0
    sum_end = 1
    current_sum = numbers[0]
    while current_sum != target_sum:
        while current_sum < target_sum:
            current_sum += numbers[sum_end]
            sum_end += 1
        while current_sum > target_sum:
            current_sum -= numbers[sum_start]
            sum_start += 1

    return numbers[sum_start:sum_end]


def main():
    data = get_input('input.txt')
    preamble = data[:25]
    numbers = data[25:]
    invalid_num = find_invlid_num(preamble, numbers)
    print(f'Part 1: {invalid_num}')
    contiguous_nums = find_contiguous_sum(data, invalid_num)
    contiguous_nums.sort()
    print(f'Part 2: {contiguous_nums[0] + contiguous_nums[-1]}')


if __name__ == '__main__':
    main()
