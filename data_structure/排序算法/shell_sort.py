def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            while (i-gap) >= 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
            print(alist)
        gap //= 2

if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(a_list)
    shell_sort(a_list)
    print(a_list)
