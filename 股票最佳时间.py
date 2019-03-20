# -*- coding: utf8 -*-


def maxProfit(prices):#时间复杂度最小
    if not prices:
        return 0
    begin_price = prices[0]
    res = 0
    for p in prices:
        if p - begin_price > res:
            res = p - begin_price
        if p < begin_price:
            begin_price = p
    return res
prices = [7,5,3,6,4,1]
d = maxProfit(prices)
print(d)
