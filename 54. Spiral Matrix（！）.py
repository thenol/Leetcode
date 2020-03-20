'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
### Never pursue the complexity of control logic


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0])

        if m==1:
            return matrix[0]
        if n==1:
            return [j for i in matrix for j in i]
        res=[]
        i=j=0
        axis=1
        i_inc=j_inc=1
        left,top=-1,0
        M,N=m+1,n
        while i<m and i>=top and j>=left and j<n: # fair status
            # move
            res.append(matrix[i][j])
            # print(i,j,'axis is: ',axis,' left and top:',left,top,matrix[i][j],M,N)
            if axis==1:
                j+=j_inc
                if j==N-1: # prepare for i asc
                    axis=0
                    i_inc=1
                    M-=1
                elif j>N-1:
                    break
                if j==left: # prepare for i dsc
                    axis=0
                    top+=1
                    i_inc=-1
            elif axis==0:
                i+=i_inc
                if i==M-1: # prepare for j dsc
                    axis=1
                    j_inc=-1
                    left+=1
                elif i>M-1:
                    break
                if i==top: # prepare for j asc
                    axis=1
                    j_inc=1
                    N-=1

            # print('---',i,j,' m and n are:',M,N,axis,i<m and i>=0 and j>=0 and j<n)
        return res
            


