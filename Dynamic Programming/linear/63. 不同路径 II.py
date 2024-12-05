"""
[medium]

给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 2 * 109。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1

https://leetcode.cn/problems/unique-paths-ii/description/
"""

# 核心思路：
"""
此题有几个注意点：
1. 初始化的时候，应该 首先初始化非法的情况 ，然后在初始化 合法的情况 ，这样一方面可以防止 越界访问 ，另一方面可以防止很多不成立的case
2. 要清楚，为什么本题没有 后效性 ，原因是每个位置可以访问的只能 往右或者往下，因此 到达目的地的路径一定是最短的 而且是最优的，因为每次移动都往终点更近一步。因此可以用case；可以和其他 表格移动类型的题目 做比较
"""

from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # state: d[i][j]表示从i,j出发的路径数量
        # 0<=i<R; 0<=j<C;
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def f(i,j):
            """表示从i,j出发的路径数量"""
            nonlocal R, C, obstacleGrid
            
            # initialization
            if i<0 or j<0 or R<=i or C<=j or obstacleGrid[i][j]==1: return 0 # 到达边界或有障碍，失败
            if i==R-1 and j==C-1: return 1 # 有一种

            # transition
            ans = 0
            ans += f(i+1, j) + f(i, j+1)

            return ans
        return f(0, 0)

