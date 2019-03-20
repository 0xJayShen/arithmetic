# -*- coding: utf8 -*-
def bubble_sort(my_list):

    for i in range(len(my_list)-1): #这个循环负责设置冒泡排序进行的次数
        for j in range(len(my_list)-i-1): # ｊ为列表下标
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


my_list = [5,2,45,6,8,2,1]

result =  bubble_sort(my_list)
print(result)