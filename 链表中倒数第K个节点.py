# -*- coding: utf8 -*-
# 两个指针，快指针先走k-1步，然后两个一起走，快指针走到尾节点时，
# 慢指针在倒数第k个节点。 需考虑k=0时和fast已经走到尾节点的情况。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def FindKthToTail( head, k):
    fast = slow = head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    return slow