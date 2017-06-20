def insert_sort(a_list):
    n = len(a_list)
    for i in range(0, n-1):
        for k in range(i+1, 0, -1):
            if a_list[k] < a_list[k-1]:
                a_list[k], a_list[k-1] = a_list[k-1], a_list[k]
            else:
                break

if __name__ == '__main__':
    one_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    one_list = [1, 10, 4, 3, 565, 323, 121, 1, 2, 3, 435, 6423, 12]
    insert_sort(one_list)
    print(one_list)
