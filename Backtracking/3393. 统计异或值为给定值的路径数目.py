"""
[medium]

给你一个大小为 m x n 的二维整数数组 grid 和一个整数 k 。

你的任务是统计满足以下 条件 且从左上格子 (0, 0) 出发到达右下格子 (m - 1, n - 1) 的路径数目：

每一步你可以向右或者向下走，也就是如果格子存在的话，可以从格子 (i, j) 走到格子 (i, j + 1) 或者格子 (i + 1, j) 。
路径上经过的所有数字 XOR 异或值必须 等于 k 。
请你返回满足上述条件的路径总数。

由于答案可能很大，请你将答案对 109 + 7 取余 后返回。

 

示例 1：

输入：grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11

输出：3

解释：

3 条路径分别为：

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
示例 2：

输入：grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2

输出：5

解释：

5 条路径分别为：

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)
(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)
(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)
示例 3：

输入：grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10

输出：0

 

提示：

1 <= m == grid.length <= 300
1 <= n == grid[r].length <= 300
0 <= grid[r][c] < 16
0 <= k < 16

https://leetcode.cn/problems/count-paths-with-the-given-xor-value/description/
"""

# 错的是多么的可笑啊

# 错误排查步骤：1.归约态；2.默认值；3.转移方程；4.调用处
# 一般有case能过了，就说明归约态和默认值以及调用处没问题，问题一般出在转移方程
from functools import cache
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_000 + 7
        m, n = len(grid), len(grid[0])
        @cache 
        def f(i, j, s):
            """从(i, j)出发到达(m-1, n-1)的路径数目"""
            if i==m-1 and j==n-1 and s^grid[i][j]==k:
                return 1
            
            ans = 0
            if i+1 < m and j < n:
                ans += f(i+1, j, s^grid[i][j])
            if j+1 < n and i < m:
                ans += f(i, j+1, s^grid[i][j])
            
            return ans % MOD
        
        return f(0, 0, 0)

    # ❌ WA：请排查找出问题所在
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        M = 10**9 + 7
        r, c = len(grid), len(grid[0])
        @cache
        def f(i, j, val):
            nonlocal M, r, c, k
            
            if i==r-1 and j==c-1 and val^grid[i][j] == k: return 1
            
            ans = 0
            
            if i+1 < r:
                ans += f(i+1, j, val^grid[i+1][j]) # ❌ 这个能是 grid[i+1][j] ？？？
            
            if j+1 < c:
                ans += f(i, j+1, val^grid[i][j+1])
            
            return ans % M
        
        return f(0, 0, 0)
        
        