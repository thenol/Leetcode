'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
'''
# Method one: using cache table
"""
思路：
1. 状态：dp[i][j] 表示区间[i,j]，左闭右闭区间，字符串是否为回文字符串
2. 状态转移方程如下
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1]*len(s) for i in range(len(s))]
        
        def dfs(s, l, r):
            if dp[l][r] > -1:
                return dp[l][r] # cache table

            if l == r:
                dp[l][r] = 1
            elif l + 1 == r:
                dp[l][r] = 1 if s[l] == s[r] else 0
            else:
                if s[l] == s[r]:
                    dp[l][r] = dfs(s, l+1, r-1)
                else:
                    dp[l][r] = 0
            
            return dp[l][r] # return state value


        mx = 0
        start, end = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(s, i, j) and j - i > mx:
                    start, end = i, j
                    mx = j - i

        return s[start:end+1]


# Method two: 填表法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        d=[[-1 for _ in range(N)] for _ in range(N)]
        mx=0
        start=end=0
        for le in range(1,N+1):
            for i in range(N-le+1):
                j=i+le-1
                d[i][j]=s[i]==s[j] and ( le < 3  or d[i+1][j-1])
                if d[i][j] and j-i>mx:
                    start,end=i,j
        return s[start:end+1]

            



       