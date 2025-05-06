"""
[hard]

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9

https://leetcode.cn/problems/n-queens/description/?envType=study-plan-v2&envId=top-100-liked
"""

from typing import List

class Solution:
    from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        求解 N 皇后问题。

        Args:
            n: 棋盘的大小 (n x n)。

        Returns:
            所有可能的 N 皇后解法的列表，每个解法表示为一个字符串列表，
            其中 'Q' 表示皇后，'.' 表示空位。
        """
        # 定义一个 lambda 函数，用于根据皇后的列位置生成棋盘行字符串
        loc = lambda x: '.' * x + 'Q' + '.' * (n - x - 1)
        res = []  # 存储所有皇后的列位置组合

        def dfs(visited_cols: List[int], path: List[tuple[int, int]], row: int) -> None:
            """
            深度优先搜索函数，尝试在每一行放置一个皇后。

            Args:
                visited_cols: 一个列表，标记哪些列已经被皇后占据。
                              初始值为全 0，当第 i 列被占据时设置为 -1。
                path: 当前已放置的皇后的坐标列表，每个元素是一个元组 (col, row)。
                row: 当前正在尝试放置皇后的行号。
            """
            # 当已经放置了 n 个皇后时，说明找到了一种有效的解决方案
            if row == n:
                res.append(path)
            else:
                # 遍历当前行的每一列
                for col in range(n):
                    # 如果当前列未被占据
                    if visited_cols[col] == 0:
                        is_safe = True  # 标记当前位置是否安全

                        # 检查当前位置是否与之前放置的皇后冲突（不在同一列或同一对角线上）
                        for prev_col, prev_row in path:
                            # 检查是否在同一对角线上：斜率的绝对值为 1
                            if abs((row - prev_row) / (col - prev_col)) == 1:
                                is_safe = False
                                break

                        # 如果当前位置安全
                        if is_safe:
                            visited_cols[col] = -1  # 标记当前列已被占据
                            dfs(visited_cols, path + [(col, row)], row + 1)  # 递归到下一行
                            visited_cols[col] = 0  # 回溯：取消当前列的占据，尝试下一个位置

        # 从第 0 行开始进行深度优先搜索
        dfs([0] * n, [], 0)

        result = []  # 存储最终的字符串形式的棋盘布局
        # 将存储的皇后列位置组合转换为字符串列表
        for placement in res:   
            board = []
            for col, _ in placement:
                board.append(loc(col))  # 使用 loc 函数生成棋盘行字符串
            result.append(board)

        return result
        