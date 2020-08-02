'''
[easy]
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        M=len(matrix)
        N=len(matrix[0])
        ans=[]
        t,b,l,r=0,M,0,N
        while True:
            for i in range(l,r): ans.append(matrix[t][i])
            t+=1
            if t>=b:break
            for i in range(t,b): ans.append(matrix[i][r-1])
            r-=1
            if l>=r:break
            for j in range(l,r)[::-1]: ans.append(matrix[b-1][j])
            b-=1
            if t>=b:break
            for j in range(t,b)[::-1]: ans.append(matrix[j][l])
            l+=1
            if l>=r:break
        return ans