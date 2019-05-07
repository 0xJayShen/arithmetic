# -*- coding: utf8 -*-
import functools
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
#层次遍历
# root为空，则返回空表
# 队列不为空，记下此时队列中的结点个数temp，temp个结点出队列的同时，
# 记录结点值，并把结点的左右子结点加入队列
# 二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。
def test(root):
    queue = [root]
    res = []
    if not root:
        return []
    while queue:
        templist = []
        templen = len(queue)
        for i in range(templen):
            temp = queue.pop(0)
            templist.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        res.append(templist)
    print(res)
    return res
test(tree)


#深度遍历
def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)

#前中后序遍历
#中序遍历:遍历左子树,访问当前节点,遍历右子树

def mid_travelsal(root):
    if root.left is not None:
        mid_travelsal(root.left)
    #访问当前节点
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

#前序遍历:访问当前节点,遍历左子树,遍历右子树

def pre_travelsal(root):
    print (root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

#后续遍历:遍历左子树,遍历右子树,访问当前节点

def post_trvelsal(root):
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print (root.value)

# 求最大树深
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
# 求两棵树是否相同
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False
# 前序中序求后序
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur
