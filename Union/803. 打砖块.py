"""
[hard]

有一个 m x n 的二元网格 grid ，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而 掉落 。一旦砖块掉落，它会 立即 从网格 grid 中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

 

示例 1：

输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。
示例 2：

输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0], 
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] 为 0 或 1
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
所有 (xi, yi) 互不相同

https://leetcode.cn/problems/bricks-falling-when-hit/description/?source=vscode
"""

# 核心思路：并查集
"""
最优解：

https://leetcode.cn/problems/bricks-falling-when-hit/solutions/561950/python-dong-hua-bing-cha-ji-zhi-guan-jie-kqoy/?source=vscode
"""
from typing import List
class UnionFind:
    def __init__(self, ):
        self.parent = {}
        self.size_of_set = {}
    
    def find(self, p):
        if self.parent[p] != p: # 惰性更新
            self.parent[p] = self.find(self.parent[p]) # 路径压缩
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            self.parent[rootQ] = rootP
            self.size_of_set[rootP] += self.size_of_set[rootQ]
            del self.size_of_set[rootQ]
    
    def get_size_of_set(self, x):
        root = self.find(x)
        return self.size_of_set[root]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def add(self, p):
        if p not in self.parent:
            self.parent[p] = p
            self.size_of_set[p] = 1


class Solution:
    def __init__(self,):
        self.CEILING = (-1, -1) # 天花板
        self.DIRECTIONS = (
            (1, 0), 
            (0, 1),
            (-1, 0),
            (0, -1),
        )

    def initialization(self, uf, m, n, grid, hits):
        """预处理，将hits从grid中打掉，并且建立并查集"""
        # 将hits从原来grid中打掉
        for i in range(len(hits)):
            x, y = hits[i]
            grid[x][y] -= 1
        
        # 构建并查集——初始化元素
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i, j))
        
        # 构建并查集——合并相邻元素
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf, i, j, m, n, grid)
        
        # 与天花板合并
        for j in range(n):
            if grid[0][j] == 1:
                uf.union(self.CEILING,(0,j))
    
    def merge_neighbors(self, uf, x, y, m, n, grid):
        for dx, dy in self.DIRECTIONS:
            i, j = x+dx, y+dy
            if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                uf.union((i, j), (x, y)) # 将自己加入并查集；⭕️都连自己，会导致parent一直变化，需要遍历该集合所有元素修改，复杂度显然很大，最好的方式，就是新来的元素，将自己parent指向已经存在的元素，而不是修改所有已经存在的元素

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        
        # 初始化
        # 构建并查集：打掉砖头，同时构建不同联通分量的并查集
        uf.add(self.CEILING)
        self.initialization(uf, m, n, grid, hits)
        print(uf.parent)

        # 合并联通分量：逆序遍历hits并且挨个加回去，
        # 并且合并联通分量，然后计算和天花板相连的集合的元素个数即为所求答案
        ans = [0] * len(hits)
        for i in range(len(hits)-1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] != 1: # 打掉的不是砖头，对结果没有影响，跳过
                continue 

            # 敲完以后与天花板连接的数量
            after_hit = uf.get_size_of_set(self.CEILING)

            uf.add((x, y))
            # 先合并周围联通分量
            self.merge_neighbors(uf, x, y, m, n, grid)
            # 再链接天花板
            if x == 0:
                uf.union(self.CEILING, (x, y))
            
            print(uf.parent)

            # 被敲的地方和天花板连接，才会对天花板的元素造成影响，否则不会有变动
            if uf.connected((x, y), self.CEILING):
                before_hit = uf.get_size_of_set(self.CEILING)
                ans[i] = before_hit-after_hit-1
        
        return ans


if __name__ == "__main__":
    s = Solution()
    res = s.hitBricks(
        # grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
        [[1,1,1],[0,1,0],[0,0,0]],
        [[0,2],[2,0],[0,1],[1,2]],

    )
    print(res)

    # [0,0,1,0]