# -*- coding: utf8 -*-
class LNode(object):
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = next
#
# link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
#
# def rev(link):
#     pre = link
#     cur = link.next
#     pre.next = None
#     while cur:
#         tmp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = tmp
#     return pre
#
# root = rev(link)
# while root:
#     print(root.data)
#     root = root.next

#递归实现

def ReverseList( pHead):
    # write code here
    if not pHead or not pHead.next:
        return pHead
    else:
        newHead = ReverseList(pHead.next)
        pHead.next.next=pHead
        pHead.next=None

        return newHead
if __name__ == '__main__':
    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)
    l1.next.next.next = LNode(99)
    l = ReverseList(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)
