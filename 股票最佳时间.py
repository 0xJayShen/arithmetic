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


#可以交易多次
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
def maxProfit( prices):
  
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

