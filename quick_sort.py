# -*- coding: utf8 -*-
def quick_sort(my_list, start, end):
    # if start == end:
    #     return False
    if start < end:
        i, j = start, end
        base = my_list[i]
        while i < j:
            while (i < j) and (my_list[j] >= base):
                j = j - 1

            my_list[i] = my_list[j]

            while (i < j) and (my_list[i] <= base):
                i = i + 1

            my_list[j] = my_list[i]
        my_list[i] = base
        quick_sort(my_list, start, i - 1)
        quick_sort(my_list, j + 1, end)

    return my_list


myList = [49, 38, 65, 97, 76, 13, 27, 49]
print("Quick Sort: ")
quick_sort(myList, 0, len(myList) - 1)
print(myList)
