# -*- coding: utf8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def PrintFromTopToBottom(root):
    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        cur = queue.popleft()
        if cur:
            res.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
    return res