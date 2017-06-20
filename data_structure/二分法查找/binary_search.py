def binary_search(a_list, item):
    n = len(a_list)
    left = 0
    right = n - 1
    while left <= right:
        middle_index = (left + right) // 2
        if a_list[middle_index] == item:
            return item
        else:
            if a_list[middle_index] > item:
                left = 0
                right = middle_index - 1
            elif a_list[middle_index] < item:
                left = middle_index + 1
                right = n - 1
    return -1


def recursion_search(a_list, item):
    n = len(a_list)
    middle_index = n // 2
    if n == 0:
        return -1
    if a_list[middle_index] == item:
        return item
    else:
        if a_list[middle_index] > item:
            return recursion_search(a_list[:middle_index], item)
        elif a_list[middle_index] < item:
            return recursion_search(a_list[middle_index + 1:], item)


if __name__ == '__main__':
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # print(binary_search(li, 55))
    # print(binary_search(li, 100))
    print(binary_search(li, 93))
    print(recursion_search(li, 210))
