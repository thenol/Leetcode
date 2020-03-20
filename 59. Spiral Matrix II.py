'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0 for _ in range(n)] for _ in range(n)] # initialization
        cur=0
        top,right,bottom,left=0,n-1,n-1,0 # boundary
        while left<=right:
            for j in range(left,right+1):
                cur+=1
                mat[top][j]=cur
            top+=1
            for i in range(top,bottom+1):
                cur+=1
                mat[i][right]=cur
            right-=1
            for j in range(right,left-1,-1): # especially pay attention to the boundary
                cur+=1
                mat[bottom][j]=cur
            bottom-=1
            for i in range(bottom,top-1,-1):
                cur+=1
                mat[i][left]=cur
            left+=1
        return mat
        