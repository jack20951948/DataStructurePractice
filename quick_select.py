

def quick_select(nums, k):
    pivot = len(nums) - k
    c = 0
    l = []
    piv = []
    r = []
    for i in nums:
        if i == nums[pivot]:
            piv.append(i)
        elif i < nums[pivot]:
            l.append(i)
        else:
            r.append(i)
            c += 1
    if c == k-1:
        return piv[0]
    elif c < k-1:
        return quick_select(l, (k-1)-c)
    else:
        return quick_select(r, k)


test_list = [10, 21, 5, 9, 13, 28, 3, 8]
print('origin list:', test_list)
print('sorted list:', quick_select(test_list, 3))