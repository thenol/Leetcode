"""
[medium]

给你一个大小为 n x n 的整数矩阵 board ，方格按从 1 到 n2 编号，编号遵循 转行交替方式 ，从左下角开始 （即，从 board[n - 1][0] 开始）的每一行改变方向。

你一开始位于棋盘上的方格  1。每一回合，玩家需要从当前方格 curr 开始出发，按下述要求前进：

选定目标方格 next ，目标方格的编号在范围 [curr + 1, min(curr + 6, n2)] 。
该选择模拟了掷 六面体骰子 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。
传送玩家：如果目标方格 next 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 next 。 
当玩家到达编号 n2 的方格时，游戏结束。
如果 board[r][c] != -1 ，位于 r 行 c 列的棋盘格中可能存在 “蛇” 或 “梯子”。那个蛇或梯子的目的地将会是 board[r][c]。编号为 1 和 n2 的方格不是任何蛇或梯子的起点。

注意，玩家在每次掷骰的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 不能 继续移动。

举个例子，假设棋盘是 [[-1,4],[-1,3]] ，第一次移动，玩家的目标方格是 2 。那么这个玩家将会顺着梯子到达方格 3 ，但 不能 顺着方格 3 上的梯子前往方格 4 。（简单来说，类似飞行棋，玩家掷出骰子点数后移动对应格数，遇到单向的路径（即梯子或蛇）可以直接跳到路径的终点，但如果多个路径首尾相连，也不能连续跳多个路径）
返回达到编号为 n2 的方格所需的最少掷骰次数，如果不可能，则返回 -1。

 

示例 1：


输入：board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。 
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。 
最后决定移动到方格 36 , 游戏结束。 
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。 
示例 2：

输入：board = [[-1,-1],[-1,3]]
输出：1
 

提示：

n == board.length == board[i].length
2 <= n <= 20
board[i][j] 的值是 -1 或在范围 [1, n2] 内
编号为 1 和 n2 的方格上没有蛇或梯子

https://leetcode.cn/problems/snakes-and-ladders/description/?source=vscode

"""

# 思路：BFS
# 为什么无法用dp，因为游戏规则规定，第一次遇到滑滑梯，必须得坐，且之后就无法坐

from typing import List
from math import ceil, inf
from functools import cache 
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        M, N = len(board), len(board[0])

        def no_to_loc(no): 
            x = M - (no-1) // N - 1 # 从下标0开始的模型
            y = (no-1) % N if (no-1)//N % 2 == 0 else N - (no-1) % N - 1
            return x, y
        
        q = deque([1])
        vis = set()
        ans = 1

        while q:
            level = len(q)
            for i in range(level):
                no = q.popleft()
                if no not in vis:
                    vis.add(no)
                    for step in range(1, 7):
                        suc = no + step
                        x, y = no_to_loc(suc)
                        if board[x][y] != -1:
                            suc = board[x][y]
                        q.append(suc)
                        if suc == M*N: # 飞完之后再检测
                            return ans
            ans += 1
        
        return -1

    # ⭕️欠缺：不能覆盖那些，回到某个点，然后再次向前试探的情况
    def snakesAndLadders_2(self, board: List[List[int]]) -> int:

        if 0<board[0][0]: return -1

        M, N = len(board), len(board[0])

        def no_to_loc(no): 
            x = M - (no-1) // N - 1 # 从下标0开始的模型
            y = (no-1) % N if (no-1)//N % 2 == 0 else N - (no-1) % N - 1
            return x, y
        
        @cache
        def f(no, fly):
            if no == M*N: return 0

            ans = inf

            x, y = no_to_loc(no)
            if 0<board[x][y] and fly: # 每一个回合能飞必须飞；
                if no<board[x][y]<= M * N : # 同时剪枝往回飞的步骤
                    ans = min(ans, f(board[x][y], 0))
                return ans # 飞完就不用再从此位置，掷骰子尝试了
            
            # 如果不能飞，只能掷骰子，即新回合开始
            for i in range(1, 7):
                if no + i <= M*N:
                    # 新回合：当前不能再飞了，需要重新掷骰子
                    ans = min(ans, f(no + i, 1) + 1) # 新回合，又可以飞了
            return ans
        ans = f(1, 1)
        return ans if ans < inf else -1

    # ❌：dp 思路   
    # WA: 没办法确保整个过程，如果遇到滑滑梯，一定坐了，换句话说，这种情况下，无法检测不可达的情况
    # 例如case: [[1,1,-1],[1,1,1],[-1,1,1]]
    # 原因：第一次遇到滑滑梯，必须得坐，这个在dp中无法控制
    def snakesAndLadders_1(self, board: List[List[int]]) -> int:
        # state: d[i][k] 表示玩家到达编号为i的位置，可以使用的k次滑滑梯
        # 1<=i<=N^2
        N = len(board)

        def convert(loc, N):
            """loc为编号，N为格子的大小"""
            row = (loc-1)//N
            col = (loc-1)%N if row%2==0 else N-(loc-1)%N-1
            return N-row-1, col

        @cache
        def f(i, k):
            """表示玩家到达编号为i的位置，可以使用的k次滑滑梯"""
            nonlocal N
            if i == 1: return 0 # 初始位置，不需要掷骰子

            ans = inf
            for j in range(1, i):
                r, c = convert(j, N)
                if 1<=i-j<=6: # 6步之内
                    ans = min(ans, f(j, k)+1)
                # 6步以内，或者6步以外都可以使用滑滑梯
                if 0<board[r][c] and 0<k and board[r][c]==i: # 可以使用滑滑梯，且可达
                    ans = min(ans, f(j, k-1))
            # 缺陷：没办法确保整个过程，如果遇到滑滑梯，一定坐了，换句话说，这种情况下，无法检测不可达的情况
            # 例如case: [[1,1,-1],[1,1,1],[-1,1,1]]
            return ans
        ans = f(N*N, 1)
        return ans if ans<inf else -1

# [[1,1,-1],[1,1,1],[-1,1,1]]
# [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
# [[-1,-1,-1],[-1,9,8],[-1,8,9]]

if __name__ == "__main__":
    res = Solution().snakesAndLadders(
        [[1,1,-1],[1,1,1],[-1,1,1]]

    )
    print(res)