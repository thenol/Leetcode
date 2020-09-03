'''
[medium]
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # d[i][j] is the maximum value 
        # d[i][j]=max(d[i-1][j],d[i][j-1])+grid[i][j]
        # d[i][0],d[0][j]
        m=len(grid)
        n=len(grid[0])
        # initializaiton:

        d=[[-1 for _ in range(n)] for _ in range(m)]
        d[0][0]=grid[0][0]
        for i in range(1,m):
            d[i][0]=grid[i][0]+d[i-1][0]
        for j in range(1,n):
            d[0][j]=grid[0][j]+d[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j]=max(d[i-1][j],d[i][j-1])+grid[i][j]
        print(d)
        return d[m-1][n-1]