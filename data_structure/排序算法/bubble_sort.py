def bubble_sort(a_list):
    n = len(a_list)
    for i in range(0, n-1):
        for j in range(1, n-1-i):
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
                # print(a_list)


if __name__ == '__main__':
    one_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    one_list = [1, 10, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 12]
    bubble_sort(one_list)
    print(one_list)
