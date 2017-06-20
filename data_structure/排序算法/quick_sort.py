def quick_sort(a_list, start, end):
    middle_element = a_list[start]
    left = start
    right = end
    if start >= end:
        return
    while left < right:
        while left < right and a_list[right] >= middle_element:
            right -= 1
        a_list[left] = a_list[right]
        while left < right and a_list[left] < middle_element:
            left += 1
        a_list[right] = a_list[left]

    a_list[left] = middle_element
    quick_sort(a_list, start, left-1)
    quick_sort(a_list, left+1, end)

if __name__ == "__main__":
    # a_list = [1, 12, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 10] 1
    # a_list = [1, 10, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 12]
    # 54
    one_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # a_list = [20, 26, 44, 17, 31, 54, 77, 55, 93] 20
    # a_list = [17, 20, 44, 26, 31, 54, 77, 55, 93] 44
    # a_list = [17, 20, 31, 26, 44, 54, 77, 55, 93] 44

    quick_sort(one_list, 0, len(one_list)-1)
    print(one_list)
