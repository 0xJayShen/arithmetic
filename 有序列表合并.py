# -*- coding: utf8 -*-
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# def mergeTwoLists(l1, l2):
#     l = head = ListNode(0)
#     while l1 and l2:
#         if l1.val <= l2.val:
#             l.next, l1 = l1, l1.next
#         else:
#             l.next, l2 = l2, l2.next
#         l = l.next
#     l.next = l1 or l2
#     return head.next
def hb(list1,list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1[0])
            del list1[0]
        else:
            result.append(list2[0])
            del list2[0]
    if list1:
        result.extend(list1)
    if list2:
        result.extend(list2)
    print(result)
    return result

list2 = [3,4,7,9,20]
list1 = [1,2,5,8,13,11]
hb(list1, list2)
