def select_sort(a_list):
    n = len(a_list)
    for i in range(0, n-1):
        small_index = i
        for j in range(i+1, n):
            if a_list[j] < a_list[small_index]:
                small_index = j
        if i != small_index:
            a_list[small_index], a_list[i] = a_list[i], a_list[small_index]

if __name__ == '__main__':
    one_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # a_list = [1, 10, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 12]
    # a_list = [111, 20, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 12]
    # a_list = [17, 20, 26, 31, 44, 55, 54, 77, 93]
    select_sort(one_list)
    print(one_list)
