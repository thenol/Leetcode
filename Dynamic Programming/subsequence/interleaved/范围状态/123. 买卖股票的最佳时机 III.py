"""
[hard]

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 105

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
"""

# 思路：
"""
输入：prices = [3,3,5,0,0,3,1,4]

指导思想：最优解一定是枚举所有暴力解下的唯一解（解的唯一性）
核心点：对于 prices[i] 需要考虑的是到底怎么决策，买入还是卖出
-> 因此就需要在当前情况下，知道左侧最大盈利 和 右侧最大盈利
-> 因此预处理，将左右侧盈利，以及最大盈利先计算出来
-> 决策，对每一个 prices[i] 来计算最大盈利，得出最后解

"""


# 方法2: 利用题目漏洞解
from math import inf
class Solution:
    # 本质：子序列问题，参见IV
    def maxProfit(self, prices: List[int]) -> int:
        # state: sell[j], buy[j]表示以prices[:cur]结尾交易j笔的最大利润
        # 0<=j<=2
        M = 2
        sell, buy = [0]*(M+1), [-inf]*(M+1)
        for i in range(len(prices)):
            for j in range(1, M+1):
                buy[j] = max(buy[j], sell[j-1]-prices[i]) # 再次买入
                sell[j] = max(sell[j], buy[j]+prices[i]) # 卖出
        return max(sell[M], buy[M])

    def maxProfit(self, prices: List[int]) -> int:
        """
        代码有点丑，可以简化
        """
        # 右侧记录最大值
        right_mx = []
        mx = -1
        for i in range(len(prices)-1, -1, -1):
            mx = max(mx, prices[i])
            right_mx.append(mx)
        
        right_mx = right_mx[::-1]
        
        # 最侧记录最小值
        left_mn = []
        mn = inf
        for i in range(len(prices)):
            mn = min(mn, prices[i])
            left_mn.append(mn)
        
        # step 1: 计算左右侧盈利：同时计算以当前股票卖出或者买入的最大盈利
        right_award = []
        left_award = []
        for i in range(len(prices)):
            la = prices[i] - left_mn[i] if prices[i] - left_mn[i] > 0 else 0
            left_award.append(la)
            ra = right_mx[i] - prices[i] if right_mx[i] - prices[i] > 0 else 0
            right_award.append(ra)
        
        # print(left_award, right_award)
        
        # step 2: 计算左右侧最大盈利：
        lma = []
        rma = []
        lmx = 0
        rmx = 0
        for i in range(len(prices)):
            # if i>=1: # 注意当前决策如果买入，则会在后续计算盈利，因此当前股票包含在右侧区间
            lmx = max(lmx, left_award[i])
            rmx = max(rmx, right_award[len(prices)-1-i])
            lma.append(lmx)
            rma.append(rmx)
        rma = rma[::-1]
        
        # step 3: 决策
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, rma[i] + lma[i]) # ❌：对于第i天的股票，不可能买入同时又卖出，其实这个地方利用了题目的漏洞：就是最优解一定不是在同一天即买入又卖出
            """
            有趣的发现：当 a<=b<=c，也就是[a...b]，中b最大，[b...c]中c最大时，交易一次和交易两次最大利益相同，即：c-b+b-a=c-a，也就是这两种情况最大利润等价，所以上面的编码结果没错

            同时题目虽然没说，当天是否能够先卖出，再买入，但是从结果上来看，两种情况确实结果相同。
            """
        
        return ans
      