"""
[medium]

在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。



每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

 

示例 1：

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
示例 2：

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
 

提示:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n - 1

https://leetcode.cn/problems/knight-probability-in-chessboard/description/?source=vscode
"""

from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # state: d[i][j][k] 表示当前位置在(i, j)移动k步的所有可能种数，以及移出棋盘的种数
        # 0<=i, j<n;0<=k
        steps = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1),
        ]
        @cache
        def f(i, j, k):
            """当前在(i,j)位置移动k步的所有可能性统计以及出盘的个数，"""
            nonlocal steps, n
            # initialization
            # 0<=i, j<n;0<=k
            if i<0 or n<=i or j<0 or n<=j: # 出局
                return (1, 0) # 只有一种，且出局
            if k == 0:
                return (1, 1) # 留在棋盘，无次数可走

            # transition
            total, stay = 0, 0
            for step in steps:
                x, y = step
                t, s = f(i+x, j+y, k-1)
                total += t
                stay += s
            
            return (total, stay)
        
        total, stay = f(row, column, k)
        # print(total, stay)
        return stay/8**k # 题目出得太蠢了，都已经出表格了，还能继续移动，这不是蠢吗
