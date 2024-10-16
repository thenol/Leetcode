"""
[medium]

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

https://leetcode.cn/problems/coin-change/description/?source=vscode
"""

# 思路：基本背包
# 状态 d[i] 很简单

# 细节易错点❌：
"""
1. 状态初始化
注意数据范围
"""

from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state: 背包问题：d[i] 表示可以凑成总金额所需的 最少的硬币个数
        # 0<=i<=10^4
        # d = [-2] * (2**31)
        # d = [-2] * (amount + 1)
        d = {}
        
        # initalization
        for coin in coins:
            d[str(coin)] = 1
        d[str(0)] = 0

        # transition
        def f(i):
            """
            d[i] 表示可以凑成总金额所需的 最少的硬币个数
            """
            if str(i) in d:
                return d[str(i)]
            
            ans = inf
            if i < 0:
                ans = -1
            else:
                for c in coins:
                    need = f(i-c)
                    if need >= 0:
                        ans = min(ans, need + 1)
            d[str(i)] = ans if ans < inf else -1
            return d[str(i)]
        
        f(amount)
        return d[str(amount)]

# 不需要考虑默认状态情况下，会少很多判断
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0] + [inf] * amount
        for x in coins:
            for c in range(x, amount + 1): # 只遍历到amount就行了，更多的情况肯定不可能构成了
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1

"""作者：灵茶山艾府
链接：https://leetcode.cn/problems/coin-change/solutions/2119065/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-21m5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""