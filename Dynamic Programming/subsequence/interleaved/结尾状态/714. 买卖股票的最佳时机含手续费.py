"""
[medium]

给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

 

示例 1：

输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
示例 2：

输入：prices = [1,3,7,5,10,3], fee = 3
输出：6
 

提示：

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?source=vscode
"""


# 核心思路：本质上是两个任意子序列的问题
# 状态转移：
#   持有股票 只能由上一个 不持有股票的状态 转移过来
#   不持有股票 只能由上一个 持有股票的状态 转移过来
# 综上所述：是两个子序列的问题

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # state: buy[i]，sell[i]分别是以i结尾代表持有和非持有股票的最大收益
        # 0<=i<N;
        N = len(prices)

        # initialization
        buy, sell = -prices[0], 0
        for i in range(1, N):
            buy = max(buy, sell-prices[i]) # 之前持有现在不新买 和 之前不持有现在购买的 最大值
            sell = max(sell, buy+prices[i]-fee) # 现在继续不持有 和 之前持有且现在不持有的 最大值
        
        return max(buy, sell)
