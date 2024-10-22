"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

 

示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
 

提示:

2 <= n <= 58

https://leetcode.cn/problems/integer-break/description/?source=vscode
"""

# 易错点❌
"""
状态理解错误导致少讨论一种情况
    关于d[i]表示什么，一个字都不能错！！！
    d[n]表示：给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。注意：!!! k>=2 !!!

    因此，本质上d[n]表示一定拆分，而少讨论了 j*(i-j) 不拆分的情况
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        # state: d[i] 表示整数i的最大化乘积
        # 0<=i<=58
        d = [0]*(n+1)

        # initialization
        ...

        # transition
        for i in range(2, n+1):
            for j in range(i+1):
                d[i] = max(j*d[i-j], d[i], j*(i-j))

        return d[n]

