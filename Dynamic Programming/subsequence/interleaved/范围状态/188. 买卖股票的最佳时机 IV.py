"""
[hard]

给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 

提示：

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/

最优解法：
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/740596/5xing-dai-ma-gao-ding-suo-you-gu-piao-ma-j6zo/?source=vscode
"""

# 思路：
"""

状态表示：
    状态变量：
        方法1: d[i][j][k] 表示从[i:j]进行k次交易，但是由于数据规模条件可知会TLE
        方法2: d[i][k] 表示[...i]上进行k次交易
    状态思考：
        考虑一般(暴力)情况下，来到每个股票价格 i 都需要考虑到两种情况下的最大盈利，就是sell or buy，因此这两种状态都需要表示


"""

# 核心思路：
"""
【本质】
    子序列问题
【状态表示】
    结尾状态表示：到当前cur范围，sell表示到当前位置手上不持有股票的最大利润，buy表示到当前位置手上持有股票的最大利润
"""

# 最优解法
class Solution:
    # 只考虑手中的钱最多，买相当于减，卖相当于加，这一次是买还是卖只与上一次是买还是卖有关
    # 整体属于dp思想，对于第i价格，利润与之前价格都有关系，所以需要buy = max(buy, ？)，sell = max(sell, ？)
    # 即dp滚动数组思想，这意味着，我们每天（第i天为结尾）都在买卖（dp就是循环推导）
    def maxProfit(self, prices: List[int]) -> int:
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    # def maxProfit(self, prices: List[int], fee: int) -> int:

        # 买卖一次
        buy, sell = -float('inf'), 0 # buy一定初始化为无穷小，因为第一次买看成手中钱减少（是个负数），sell初始化小于等于0
        for p in prices:
            buy = max(buy, 0-p) # 由于只能买一次，买之前手里只有0元，买之后手里有max(buy, 0-p)
            sell = max(sell, buy+p) # 卖之前一定是买buy，卖完手里有max(sell, buy+p)
        return sell

        # 不限制买卖次数
        # buy, sell = -float('inf'), 0
        # for p in prices:
        #     buy = max(buy, sell-p) # 由于不限制交易次数，买之前可能是卖过手里的钱sell，买之后max(buy, sell-p)
        #     sell = max(sell, buy+p) # 卖之前一定是买buy，卖完手里有max(sell, buy+p)
        # return sell 

        # 买卖两次
        # buy1, sell1, buy2, sell2 = -float('inf'), 0, -float('inf'), 0
        # for p in prices:
        #     buy1 = max(buy1, 0-p) # 同理，第一次交易，手上是没有钱的
        #     sell1 = max(sell1, buy1+p) # 第一次卖出，一定从第一次买入转移而来，或者一直不交易
        #     buy2 = max(buy2, sell1-p) # 第二次买入，必须基于第一次卖出
        #     sell2 = max(sell2, buy2+p) # 整体而言，这次操作只与上一次有关
        # return sell2

        # 买卖k次
        # buy = [-float('inf')] * (k+1)
        # sell = [0] * (k+1) # 初始化为k+1，是因为第一次买，是0-p，这里我们sell[0]=0，就可以了
        # for p in prices:
        #     for k in range(1, k+1): # buy[0]和sell[0]作为边界初始化
        #         buy[k] = max(buy[k], sell[k-1]-p) # 第一次sell[i-1]=sell[0]=0；第k次买，一定基于第k-1次卖
        #         sell[k] = max(sell[k], buy[k]+p) # 第k次卖一定基于第k次买
        # return sell[-1]

        # 不限制买卖次数，冻结期为1天
        # buy, sell_pre, sell_now = -float('inf'), 0, 0 
        # # 冻结期为1天，意味着，我们买的上一个状态不能是上一次卖的，而是上上次卖的；说白了，限制当前买入，只能基于上上次的卖出，也就是buy[now]只能依赖sell[now-2]，而不是sell[now-1]，本质是限制状态转移
        # # 至此，要理解，这是dp滚动数组思想，这意味着，我们每天都在买卖
        # for p in prices:
        #     buy = max(buy, sell_pre-p) # 这次买的是接着上上次卖的，可以理解为buy[i]与sell[j-1]有关，而不是sell[j]
        #     sell_pre = sell_now # 因为后面要更新sell_now，这里要先保存，buy[i-1]的记录
        #     sell_now = max(sell_now, buy+p)
        # return sell_now

        # 不限制买卖次数，但是有手续费
        # buy, sell = -float('inf'), 0
        # for p in prices:
        #     buy = max(buy, sell-fee-p) # 多减去手续费即可
        #     sell = max(sell, buy+p)
        # return sell