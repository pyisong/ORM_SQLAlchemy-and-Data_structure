def merge_sort(a_list):
    n = len(a_list)
    if n == 1:
        return a_list
    middle = n//2
    left_part = merge_sort(a_list[: middle])
    right_part = merge_sort(a_list[middle:])
    left_length = len(left_part)
    right_length = len(right_part)
    sorted_list = []
    i = 0
    j = 0

    while i < left_length and j < right_length:
            if left_part[i] <= right_part[j]:
                sorted_list.append(left_part[i])
                i += 1
            elif left_part[i] > right_part[j]:
                sorted_list.append(right_part[j])
                j += 1

    sorted_list += left_part[i: middle]
    sorted_list += right_part[j:]
    return sorted_list

if __name__ == '__main__':
    one_list = [54, 26, 93, 17, 31, 44, 55, 20]
    print(merge_sort(one_list))
