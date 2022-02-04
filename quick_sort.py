import random

def quick_sort(nLst):
    if len(nLst) <= 1:
        return nLst
    
    left = []
    right = []
    piv = []
    pivot = random.choice(nLst)
    for i in nLst:
        if i == pivot:
            piv.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + piv + quick_sort(right)


test_list = [10, 21, 5, 9, 13, 28, 3, 8]
print('origin list:', test_list)
print('sorted list:', quick_sort(test_list))