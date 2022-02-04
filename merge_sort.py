def merge(left_list, right_list):
    output = []
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            output.append(left_list.pop(0))
        else:
            output.append(right_list.pop(0))
    if left_list:
        output += left_list
    if right_list:
        output += right_list
    return output

def merge_sort(nLst):
    if len(nLst) <= 1:
        return nLst
    mid = len(nLst) // 2
    left = nLst[:mid]
    right = nLst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


test_list = [10, 21, 5, 9, 13, 28, 3, 8]
print('origin list:', test_list)
print('sorted list:', merge_sort(test_list))