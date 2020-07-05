'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 0:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        col_zero={i:0 for i in range(n)}
        row_zero={i:0 for i in range(m)}
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if not col_zero[j]==1:
                        col_zero[j]=1
                    if not row_zero[i]==1:
                        row_zero[i]=1
        for k,v in col_zero.items():
            if v==1:
                for _ in range(m):
                    matrix[_][k]=0
        for k,v in row_zero.items():
            if v==1:
                for _ in range(n):
                    matrix[k][_]=0
        
        return matrix


# version 1:
