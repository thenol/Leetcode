"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2

https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked
"""

from typing import List

class Solution:
    # 时间复杂度 O(mn)；空间复杂度 O(mn)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        计算所有新鲜橘子腐烂所需的最少分钟数。

        Args:
            grid: 一个二维整数网格，其中:
                  0 代表一个空单元格。
                  1 代表一个新鲜的橘子。
                  2 代表一个腐烂的橘子。

        Returns:
            返回所有新鲜橘子腐烂所需的最少分钟数。如果不可能，则返回 -1。
        """
        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数
        fresh = 0  # 初始化新鲜橘子的数量
        q = []  # 初始化一个队列，用于存储腐烂橘子的坐标

        # 遍历网格，统计新鲜橘子的数量并将初始腐烂的橘子加入队列
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1  # 统计新鲜橘子个数
                elif x == 2:
                    q.append((i, j))  # 将初始腐烂的橘子的坐标加入队列

        ans = 0  # 初始化腐烂所需的时间
        while q and fresh:  # 当队列不为空且还有新鲜橘子时；✅本质：层次遍历；另外，假如fresh，可以实现提前终止循环，降低复杂度
            ans += 1  # 时间增加一分钟
            tmp = q  # 创建一个临时队列，存储当前分钟需要处理的腐烂橘子；凡事在队列中的一定是腐烂的橘子
            q = []  # 清空主队列，用于存储下一分钟新腐烂的橘子
            for x, y in tmp:  # 遍历当前所有腐烂的橘子
                # 检查当前腐烂橘子周围的四个方向
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    # 判断相邻位置是否在网格内且是新鲜橘子
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1: # 新鲜的橘子腐烂之后再加入队列，可以降低复杂度
                        fresh -= 1  # 新鲜橘子数量减一
                        grid[i][j] = 2  # 将新鲜橘子标记为腐烂
                        q.append((i, j))  # 将新腐烂的橘子加入队列，等待下一轮腐烂

        # 如果最终还有新鲜橘子，说明无法全部腐烂，返回 -1；否则返回腐烂所需的时间
        return -1 if fresh else ans # ⭕️注意返回值，也可能存在无法腐烂的情况
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0 
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        ans = 0
        while q and fresh:
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x-1, y), (x+1, y), (x, y+1), (x, y-1):
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i, j))
            ans += 1
        return -1 if fresh else ans
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        朴素方法：
            1. 初始化一个 分钟数组
            2. 针对每一个腐烂句子进行深度遍历，更新分钟数组
        
        时间复杂度：O(腐烂个数 * m * n)
        空间复杂度 O(mn)
        """