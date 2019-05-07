# -*- coding: utf8 -*-
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


n1 = Node("n1", None)
n2 = Node("n2", n1)
n3 = Node("n3", n2)
n4 = Node("n4", n3)
n5 = Node("n5", n4)

head = n5  # 链表的头节点

P1 = head  # 一次步进1个node
P2 = head  # 一次步进2个node

while P2.next is not None and P2.next.next is not None:
    P2 = P2.next.next
    P1 = P1.next
print(P1.data)
