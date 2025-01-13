"""
[hard]

在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

 

示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
示例 2：

输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径： 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
示例 3：

输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。
 

提示：

1 <= grid.length * grid[0].length <= 20

https://leetcode.cn/problems/unique-paths-iii/description/?source=vscode
"""

from functools import cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        vis = defaultdict(int)
        steps = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        avail_cnt = 0

        M, N = len(grid), len(grid[0])
        start, end = None, None
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    avail_cnt += 1        

        vis[start] = 1 # 从起点开始

        def f(i, j, cnt):
            # print(dict(vis), (i,j), cnt, avail_cnt)
            """从(i,j)出发到达终点的个数"""
            if (i, j) == end and cnt == 0: return 1 # 到2，即0和2的个数

            ans = 0
            for step in steps:
                dx, dy = step
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N and not vis[(x, y)] and 0 <= grid[x][y] and 0<=cnt-1:
                    vis[(x, y)] = 1 # 尝试step
                    ans += f(x, y, cnt-1)
                    vis[(x, y)] = 0 # 尝试完复位

            return ans
        
        return f(*start, avail_cnt+1) # 多加一个，是因为最后访问到2

    # 究竟错在哪里 ？要么初始化，要么转移方程
    # 以及如何纠错 ？
    # 易错点❌：方格遍历，是有后效性的
    # 所以不能cache啊，老铁
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # state: 
        r, c = len(grid), len(grid[0])
        visited = [[0]*c for _ in range(r)]
        cnt = 0
        # 统计0的个数
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0: cnt+=1
                if grid[i][j] == 1:
                    start = (i, j)
        # ⭕️：经过所有从1出发，经过所有0，到达2，共经过 cnt+1 步；到底该取几，特殊值一代入，就可以验证出来啦！！！

        # @cache 
        # ❌：方格遍历决策，是有后效性的啊，不能cache
        def f(i, j, steps):
            """返回方法数"""
            nonlocal grid, r, c, visited

            # initial
            if i<0 or j<0 or r<=i or c<=j: return 0
            if visited[i][j] or grid[i][j] == -1: return 0 # 访问过了或者无法访问，失败
            # print(visited, i, j, grid[i][j], steps)
            if grid[i][j] == 2 and 0 < steps: return 0
            if grid[i][j] == 2 and steps==0: return 1 # 找到一种

            # transition
            ans = 0
            visited[i][j] = 1 # 
            ans += f(i-1, j, steps-1) + f(i+1, j, steps-1) + f(i, j-1, steps-1) + f(i, j+1, steps-1)

            visited[i][j] = 0

            return ans
        x, y = start
        return f(x, y, cnt+1)
