# -*- coding: utf8 -*-
#每个物体就一个
C = [3,2,6,7,1,4,9,5]#cost 单个物品所占容量
V = [6,3,5,8,3,1,6,9]#每个物品的价值
target = 15 #背包容量
F = [0 for i in range(0,target+1)] #初始化 元素个数为背包大小加1（target+1）
n = len(C)

def ZeroOneBackPack(cost,value):
    for i in reversed(range(cost,target+1)): #逆序遍历
        F[i] = max(F[i],F[i-cost]+value)

for i in range(0,n):
    ZeroOneBackPack(C[i],V[i])
print (F[target])

#可以取无数多个
# C = [3,2,6,7,1,4,9,5]
# V = [6,3,5,8,3,1,6,9]
# target = 15
# F = [0 for i in range(0,target+1)]
# n = len(C)
#
# def CompleteBackPack(cost,value):
#     for i in range(cost,target+1):#这是和01背包唯一的区别 正序遍历
#         F[i] = max(F[i],F[i-cost]+value)
#
# for i in range(0,n):
#     CompleteBackPack(C[i],V[i])
# print (F[target])