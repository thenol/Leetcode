'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dynamic programming:from top to bottom:fill in the table

        m=len(triangle)
        for i in range(m-1): # i th row
            for j in range(i+2): # i+1 th row
                if j==0:
                    triangle[i+1][j]=triangle[i+1][j]+triangle[i][j]
                elif j==i+1:
                    triangle[i+1][j]=triangle[i+1][j]+triangle[i][j-1]
                else:
                    triangle[i+1][j]=min(triangle[i+1][j]+triangle[i][j],triangle[i+1][j]+triangle[i][j-1])
        
        return min(triangle[-1])

