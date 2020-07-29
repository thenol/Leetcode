'''
[hard]
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# version 1:  TLE, dp without memory
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dynamic programming
        def dp(i,j,k):
            if i==len(s1)-1 and j==len(s2)-1 and k==len(s3)-1:
                return True
            if i<len(s1) and j<len(s2):
                if s3[k]==s1[i] and s3[k]==s2[j]:
                    return dp(i+1,j,k+1) or dp(i,j+1,k+1)
                elif s3[k]==s1[i]:
                    return dp(i+1,j,k+1)
                elif s3[k]==s2[j]:
                    return dp(i,j+1,k+1)
                else:
                    return False
            elif i>=len(s1):
                return s2[j:]==s3[k:]
            elif j>=len(s2):
                return s1[i:]==s3[k:]

        if not len(s1)+len(s2)==len(s3):
            return False
        else:
            return dp(0,0,0)


# version 2: dp iteration
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dynamic programming
        M=len(s1)
        N=len(s2)
        if M+N!=len(s3):
            return False
        if M==0:return s2==s3
        if N==0:return s1==s3

        # bounary initialization
        f=[[False for _ in range(N+1)] for _ in range(M+1)]
        for i in range(M): # row
            if s1[i]==s3[i]:
                f[i+1][0]=True
            else:
                break
        for i in range(N):# column
            if s2[i]==s3[i]:
                f[0][i+1]=True
            else:
                break
        f[0][0]=True

        # transition formula
        for i in range(1,M+1):
            for j in range(1,N+1):
                f[i][j]=(s1[i-1]==s3[i+j-1] and f[i-1][j]) or (s2[j-1]==s3[i+j-1] and f[i][j-1])
                
        return f[M][N]


# version 3: space optimization: Scrolling array
