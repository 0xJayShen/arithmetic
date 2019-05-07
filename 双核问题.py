# -*- coding: utf8 -*-
w = [0, 3072, 3072, 7168, 3072, 1024]  # 假设进入处理的的任务大小
w = map(lambda x: x / 1024, w)  # 转化下
p = w  # 这题的价值和任务重量一致
n = sum(w) / 2 + 1  # 背包承重为总任务的一半

optp = [[0 for j in range(n + 1)] for i in range(len(w))]

for i in range(1, len(p)):
    for j in range(1, n + 1):
        if j >= p[i]:
            optp[i][j] = max(optp[i - 1][j], p[i] + optp[i - 1][j - w[i]])
        else:
            optp[i][j] = optp[i - 1][j]

print(optp[-1][-1])
print(optp)
