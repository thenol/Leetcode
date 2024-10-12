"""
[medium]

给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 104
"""

# 思路：
"""
数据规模：
    时间复杂度必须低于O(n^2)
状态表示：
    毫无疑问，只有一个变量，因此d[i] 和为 i 的完全平方数的最少数量 

状态转移：
    只需要聚焦分解，能做的简单策略就加上，从而能够有效过滤数据规模，降低时间复杂度

初始化：
    ...
"""

from math import inf
class Solution:
    def numSquares(self, n: int) -> int:
        # state: d[i] 和为 i 的完全平方数的最少数量 
        # 0<=i<=n
        d = [-1] * (n+1)

        # initialization
        d[0] = 1
        for i in range(1, n+1):
            if i*i < n+1:
                d[i*i] = 1


        # transition
        def f(i):
            # 平方数已经初始化
            if d[i] >= 0:
                return d[i]

            ans = inf
            # 非平方数
            for j in range(1, i+1):
                if j*j < i: # 直接分解，降低时间复杂度
                    ans = min(ans, 1 + f(i-j*j))
                else:
                    break

            d[i] = ans
            return d[i]
        
        f(n)
        # print(d)
        return d[n]