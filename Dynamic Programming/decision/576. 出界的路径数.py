"""
[medium]

给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。

 

示例 1：


输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6
示例 2：


输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12
 

提示：

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

https://leetcode.cn/problems/out-of-boundary-paths/description/?source=vscode
"""

from functools import cache
N = 10**9 + 7
@cache
def f(m, n, i, j, k):
    """表示i,j处，还可以移动k次的个数"""
    if i<0 or j<0 or m<=i or n<=j:
        return 1
    if k == 0: return 0
    if 0<k:
        ans = 0
        ans += f(m, n, i-1, j, k-1) 
        ans += f(m, n, i+1, j, k-1) 
        ans += f(m, n, i, j-1, k-1) 
        ans += f(m, n, i, j+1, k-1)
    return ans % N

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # state: d[i][j][k]表示i,j处，还可以移动k次的个数
        return f(m, n, startRow, startColumn, maxMove)

# 易错点❌：
#   此题还有另外一种编写方式：就是从正面分析，代码如下
"""
def f(i, j, k):
    "表示i,j处，还可以移动k次的个数"
    ans = 0
    if k >= 1:
        if (i in {0, m-1} or j in {i, n-1}):
        # 只剩一步，且在边界；否则移动不出边界
            if (i,j) in [(0, 0), (0, n-1), (m-1, 0), (m-1, n-1)]:
                # 在四个拐角
                ans += 2
            else:
                # 只能在边界，但是不在拐角
                ans +=1 
        else: # 不在边界，可以随便走
"""
# 注意这种方式，如果想着处理边界情况，需要讨论的情况很多，也就是试图控制在边界的走向，这样容易重复，而且很复杂
# 然而，从反面方法，也就是从出界的角度考虑，只要出界就是一种，这样讨论不重不漏，四种情况