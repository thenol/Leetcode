"""
[hard]

给你一个 n x n 的网格 grid ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：

0 表示这个格子是空的，所以你可以穿过它。
1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
-1 表示这个格子里有荆棘，挡着你的路。
请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：

从位置 (0, 0) 出发，最后到达 (n - 1, n - 1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 0 或者 1 的格子）；
当到达 (n - 1, n - 1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 0 ）；
如果在 (0, 0) 和 (n - 1, n - 1) 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。
 

示例 1：


输入：grid = [[0,1,-1],[1,0,-1],[1,1,1]]
输出：5
解释：玩家从 (0, 0) 出发：向下、向下、向右、向右移动至 (2, 2) 。
在这一次行程中捡到 4 个樱桃，矩阵变成 [[0,1,-1],[0,0,-1],[0,0,0]] 。
然后，玩家向左、向上、向上、向左返回起点，再捡到 1 个樱桃。
总共捡到 5 个樱桃，这是最大可能值。
示例 2：

输入：grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
输出：0
 

提示：

n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] 为 -1、0 或 1
grid[0][0] != -1
grid[n - 1][n - 1] != -1

https://leetcode.cn/problems/cherry-pickup/description/?source=vscode
"""

# 最优解：
"""
https://leetcode.cn/problems/cherry-pickup/solutions/2766975/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-ruue/?source=vscode
"""

# ⭕️两次dp的两次最优 不等于 全局最优；即 局部最优 不等于 全局最优

from math import inf
from functools import cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        @cache
        def f(i, j, x, y):
            """i, j为第一个人坐标， x, y为第二个人坐标"""
            if i==R-1 and j==C-1: return grid[i][j]

            ans = -inf # 如果初始化为0，会导致无法到达的也可以采摘到樱桃
            for a, b in [[i+1, j], [i, j+1]]:
                for c, d in [[x+1, y], [x, y+1]]:
                    if 0<=a<R and 0<=b<C and 0<=c<R and 0<=d<C and -1<grid[a][b] and -1<grid[c][d]:
                        ans = max(ans, f(a, b, c, d))
            ans += grid[i][j] + (grid[x][y] if i!=x and j!=y else 0) # 重复只能计算一次
            return ans
        ans = f(0, 0, 0, 0)
        return ans if -inf < ans else 0
