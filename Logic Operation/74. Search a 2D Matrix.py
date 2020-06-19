'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search algorithm
        if not matrix:
            return False
        if not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        def binsearch(arr,target):
            l,r=0,len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]>target:
                    r=mid-1
                elif arr[mid]<target:
                    l=mid+1
                elif arr[mid]==target:
                    return True
            return False
        for i in range(m):
            if matrix[i][0]<=target and matrix[i][n-1]>=target:
                return binsearch(matrix[i],target)
        return False