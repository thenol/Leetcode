'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# graph-theory:  the number of the connected graphs 

class Solution:
    # 单独的vis数组，空间复杂度较高
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        M=len(grid)
        N=len(grid[0]) 
        vis=[[0 for _ in range(N)] for _ in range(M)] # 用了单独的vis数组
        def dfs(i,j):
            nonlocal vis,M,N
            if i<M and j<N and i>=0 and j>=0 and vis[i][j]==0 and grid[i][j]=='1':
                vis[i][j]=1
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        
        ans=0
        for i in range(M):
            for j in range(N):
                if vis[i][j]==0 and grid[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans
    
    # 原地修改数组，空间复杂度较低
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            # 出界，或者不是 '1'，就不再往下递归
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'  # 插旗！避免来回横跳无限递归
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走

        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '1':  # 找到了一个新的岛
                    dfs(i, j)  # 把这个岛插满旗子，这样后面遍历到的 '1' 一定是新的岛
                    ans += 1
        return ans
