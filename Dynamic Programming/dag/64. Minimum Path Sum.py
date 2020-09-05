'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dynamic programming, from bottom to top
        m=len(grid)
        n=len(grid[0])
        d=[[grid[m-1][n-1] for _ in range(n)] for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                updated=False
                if i+1<m:
                    d[i][j] = d[i+1][j]+grid[i][j] # right first
                    updated=True
                if j+1<n:
                    d[i][j] = min(d[i][j+1]+grid[i][j],d[i][j]) if updated else d[i][j+1]+grid[i][j] # bottom second
        return d[0][0]


# # version C++:
# class Solution {
# public:
#     int minPathSum(vector<vector<int>>& grid) {
#         int m=grid.size();
#         int n=grid[0].size();
#         // vector<vector<int>> f(m+1,vector<int>(n+1,10000));
#         // f[0][1]=f[1][0]=0;
#         vector<int>f(n+1,1000);
#         f[1]=0;
#         for(int i =1;i<=m;i++){
#             for(int j=1;j<=n;j++){
#                 // f[i][j]=min(f[i-1][j],f[i][j-1])+grid[i-1][j-1];    
#                 f[j]=min(f[j],f[j-1])+grid[i-1][j-1];    
#             }
#         }
#         // return f[m][n];
#         return f[n];
#     }
# };