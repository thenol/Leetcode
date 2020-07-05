'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numSquares(self, n: int) -> int:
        # knapsack
        f=[n]*(n+1)
        f[0]=0 # initial
        v=[]
        tmp=0
        for i in range(n):
            if i**2<=n:
                v.append(i**2)
            else:
                break
        N=len(v)
        for i in range(N):
            for j in range(v[i],n+1):
                f[j]=min(f[j],f[j-v[i]]+1) # Recursive formula
        # print(f[n])
        return f[n]