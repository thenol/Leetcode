"""
[easy]

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ❌state: sell, buy 表示以当前结尾的非持有和持有状态最优解，注意只能交易一次；❗️不限制买卖次数
        # sell, buy = 0, -prices[0]
        # for i in range(len(prices)):
        #     sell = max(sell, buy+prices[i])
        #     buy = max(buy, sell-prices[i])
        
        # return max(sell, buy)

        # ✅state: sell 表示以当前结尾的不持有的最优解；❗️限制一次
        left_min = 10**4
        sell = 0
        for i in range(len(prices)):
            sell = max(sell, prices[i]-left_min)
            left_min = min(left_min, prices[i])
        
        return sell