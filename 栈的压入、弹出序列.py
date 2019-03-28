# -*- coding: utf8 -*-
# https://leetcode.com/problems/validate-stack-sequences/
def validateStackSequences( pushed ,popped) :
    stack = []
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)

validateStackSequences([1,2,3,4,5],[4,5,3,2,1])