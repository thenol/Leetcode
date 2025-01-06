"""
[medium]

给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。

岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。

你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。

返回必须翻转的 0 的最小数目。

 

示例 1：

输入：grid = [[0,1],[1,0]]
输出：1
示例 2：

输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
示例 3：

输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1
 

提示：

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] 为 0 或 1
grid 中恰有两个岛

https://leetcode.cn/problems/shortest-bridge/description/?source=vscode
"""

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        steps = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 1:
                    continue
                
                # step 1: 找到第一个岛屿
                q = deque([(i, j)])
                island  = []

                """
                # TLE版本 ❌
                while q:
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        grid[x][y] = -1 # 访问
                        island.append((x, y))
                    for dx, dy in steps:
                        x1, y1 = x+dx, y+dy
                        if 0<=x1<M and 0<=y1<N and grid[x1][y1] == 1:
                            q.append((x1, y1)) # 不提前更新，会导致不必要的重复访问海洋节点，就是一些节点被反复加入队列中

                # 改进
                que = set({(i,j)})
                while q:
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        grid[x][y] = -1 # 访问
                        island.append((x, y))
                    for dx, dy in steps:
                        x1, y1 = x+dx, y+dy
                        if 0<=x1<M and 0<=y1<N and grid[x1][y1] == 1 and (x1, y1) not in que:
                            q.append((x1, y1))
                            que.add((x1,y1)) # 表示已经加入队列中的岛屿，即discover
                """
                
                grid[i][j] = -1
                while q:
                    x, y = q.popleft()
                    island.append((x, y))
                    for dx, dy in steps:
                        x1, y1 = x+dx, y+dy
                        if 0<=x1<M and 0<=y1<N and grid[x1][y1] == 1:
                            grid[x1][y1] = -1 # 提前表示状态，类似discover，第二次再遇到，就不会在加入队列；同时改变小岛的状态为-1，一石二鸟
                            q.append((x1, y1))
                
                # step 2: 计算距离
                ans = 0
                while island:
                    level = len(island)
                    for i in range(level):
                        x, y = island.pop(0)
                        for dx, dy in steps:
                            x1, y1 = x+dx, y+dy
                            if 0<=x1<M and 0<=y1<N and 0<=grid[x1][y1]:
                                if grid[x1][y1] == 1:
                                    return ans
                                if grid[x1][y1] == 0:
                                    grid[x1][y1] = -1
                                island.append((x1,y1))
                    ans += 1
                