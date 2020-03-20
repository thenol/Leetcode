'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dynamic programming, from the bottom to top

        d=[[0 for _ in range(n)] for _ in range(m)]

        d[m-1][n-1]=1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j+1<n:
                    d[i][j]+=d[i][j+1]
                if i+1<m:
                    d[i][j]+=d[i+1][j]
                # print(i,j,'val: ',d[i][j])

        return d[0][0] if d[0][0]<=2*10**9 else 2*10**9