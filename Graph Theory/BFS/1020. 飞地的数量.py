"""
[medium]

给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

 

示例 1：


输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
示例 2：


输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] 的值为 0 或 1

https://leetcode.cn/problems/number-of-enclaves/description/?source=vscode
"""


from functools import cache
from collections import defaultdict
class Solution:
    # 遇到图相关问题，不用想了，铁定图的遍历算法
    # 逆向思维：反向寻找，直接从边界往里面去寻找
    def numEnclaves(self, grid: List[List[int]]) -> int:
        action_list = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
        ]
        
        m, n = len(grid), len(grid[0])
        vis = defaultdict(int)

        # ⭕️注意存在后效性，无法cache
        def f(x, y):
            """从(x, y)出发，只要遇到1就可以"""
            if grid[x][y]:
                vis[(x,y)] = 1
                for dx, dy in action_list:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] and not vis[(x+dx, y+dy)]:
                        vis[(x+dx, y+dy)] = 1
                        f(x+dx, y+dy)
        
        ans = 0
        for i in range(m):
            f(i, 0)
            f(i, n-1)
        
        for j in range(n):
            f(0, j)
            f(m-1, j)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not vis[(i, j)]:
                    ans += 1
        return ans


    # method 1: 暴力回溯，O(N^3)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        action_list = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
        ]
        
        m, n = len(grid), len(grid[0])
        vis = defaultdict(int)

        # ⭕️注意存在后效性，无法cache
        def f(x, y):
            """从(x, y)出发是否可以到达边界"""
            if x<0 or m<=x or y<0 or n<=y:
                return True

            if vis[(x, y)] or not grid[x][y]: return False
            
            ans = False
            vis[(x, y)] = 1
            for dx, dy in action_list:
                ans = ans or f(x+dx, y+dy)
            vis[(x, y)] = 0
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not f(i, j):
                    print(i, j, f(i, j))
                    ans += 1
        
        return ans