"""
[meidum]

给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
示例 2:

输入: prices = [1]
输出: 0
 

提示：

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
"""

# 核心思路：
#   状态表示：构建当前持有股票的最大利润 buy，和不持有股票的最大利润 sell 状态


from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: sell为当前未持有股票的最大收益，buy为当前持有当前股票的最大收益，注意持有不持有当前股票，得看实际计算的利润

        # 冷冻期的本质含义是：当前买入股票状态依赖于，两天前不持有股票的状态
        
        # initialization
        sell, buy, last_trade = 0, -inf, 0

        # transition
        for i in range(len(prices)):
            buy = max(buy, last_trade - prices[i])
            last_trade, sell = sell, max(sell, buy + prices[i])

        return sell

    # 与上述一致
    def maxProfit(self, prices: List[int]) -> int:
        # state:  sell, buy表示到当前位置，手上不持有和持有的最大利润
        sell, buy = 0, -inf
        last_sell = 0
        for i in range(len(prices)):
            buy = max(buy, last_sell-prices[i]) # 依赖于前一天的卖出
            last_sell = sell # 记录下前一天的卖出最大收益，即更新今天的之前先记录昨天的
            sell = max(sell, buy+prices[i]) # 依赖于当前持有最大利润，更新当前卖出最大收益

        return max(sell, buy)