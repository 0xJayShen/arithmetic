# -*- coding: utf8 -*-
#values是硬币的面值values = [ 25, 21, 10, 5, 1]
#valuesCounts   钱币对应的种类数
#money  找出来的总钱数
#coinsUsed   对应于目前钱币总数i所使用的硬币数目
# 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
def coinChange(values,valuesCounts,money,coinsUsed):
    #遍历出从1到money所有的钱数可能
    for cents in range(1,money+1):
        minCoins = cents
        #把所有的硬币面值遍历出来和钱数做对比
        for kind in range(0,valuesCounts):
            if (values[kind] <= cents):
                temp = coinsUsed[cents - values[kind]] +1
                if (temp < minCoins):
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print ('面值:{0}的最少硬币使用数为:{1}'.format(cents, coinsUsed[cents]))
if '__name__ = __main__':
    values = [ 25, 21, 10, 5, 1]
    money = 63
    coinsUsed= [0]*(money+1)
    len  = len(values)
    coinChange(values, len, money, coinsUsed)