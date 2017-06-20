def find_element(alist, item):
    """利用改进的二分查找"""
    left = 0
    right = len(alist) - 1
    while left <= right:
        # 求中间位置mid
        mid = (left + right) // 2
        # 中间位置恰好是要查找的元素，返回此位置
        if alist[mid] == item:
            return mid
        # 如果要查找的item比中间位置元素大
        elif item > alist[mid]:
            # alist[mid]<alist[left]说明右边是有序的，item>alist[right]说明item在mid的左边
            if alist[mid] < alist[left] and item > alist[right]:
                right = mid - 1
            # 否则item在mid的右边
            else:
                left = mid + 1
        # item<=alist[mid]
        else:
            # alist[mid]>=alist[left]说明左边是有序的，item<alist[left]说明item在mid的右边
            if alist[mid] >= alist[left] > item:
                left = mid + 1
            # 否则item在mid的左边
            else:
                right = mid - 1
    # 未找到，返回-1
    return -1

if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6]
    result = find_element(a_list, 6)
    print(result)
