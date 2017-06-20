def select_elements(n):
    while n > 0:
        t_list = []
        try:
            for i in range(len(a_list)):
                for j in range(len(a_list)):
                    if a_list[i] > a_list[j]:
                        break
                    if j == len(a_list) - 1:
                        min_list.append(a_list[i])
                        temp = a_list[i]
                        n -= 1
                        a_list.remove(temp)
                        t_list.append(temp)
                if len(t_list) > 0:
                    break
        except IndexError:
            pass
    return min_list

if __name__ == "__main__":
    a_list = [1, 1, 1, 1, 1, 3, 5, 8, 6, 7, 10, 1]
    min_list = []
    temp_list = select_elements(3)
    print(temp_list)
