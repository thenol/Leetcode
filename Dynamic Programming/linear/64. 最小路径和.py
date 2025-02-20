"""
[medium]

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

https://leetcode.cn/problems/minimum-path-sum/description/
"""

# 类比：《63. 不同路径 II.py》

from functools import cache
from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # d[i][j]表示从左上角到当前位置路径上的数字总和为最小。
        # 0<=i<R;0<=j<C
        R, C = len(grid), len(grid[0])
        @cache
        def f(i, j):
            """从左上角到当前位置路径上的数字总和为最"""
            nonlocal R, C, grid

            # initialization
            if i<0 or j<0 or R<=i or C<=j: return inf # 边界情况; ✅：grid类型题目中，这种提前判断的方式可以大大简化后续坐标的判断逻辑
            if i==0 and j==0: return grid[0][0]

            # transition
            return min(f(i-1, j), f(i, j-1)) + grid[i][j]
        return f(R-1, C-1)
