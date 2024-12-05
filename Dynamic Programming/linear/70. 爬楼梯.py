"""
[easy]

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 

提示：

1 <= n <= 45

https://leetcode.cn/problems/climbing-stairs/description/
"""

# ⭕️：最后一步是确定的

from functools import cache
class Solution:
    # 记忆化搜索
    def climbStairs_2(self, n: int) -> int:
        @cache
        def f(i):
            if i==1: return 1
            if i==2: return 2
            return f(i-1)+f(i-2)
        
        return f(n)
        
    # 迭代法
    def climbStairs(self, n: int) -> int:
        # state: d[i]表示到i阶共有集中方法
        # 0<=i<=n
        d = [0]*(n+1)

        # initialization
        d[0] = 1

        # transition
        for i in range(n+1):
            for j in range(1, 3):
                if 0<=i-j: # i-j1
                    d[i] += d[i-j] # 1<=j<=2; 最后一步是确定的
        return d[n]
