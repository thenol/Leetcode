"""
[medium]

给你一个字符串 s，找到 s 中最长的 
回文
 
子串
。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成

https://leetcode.cn/problems/longest-palindromic-substring/description/
"""

from functools import cache
class Solution:
    # method 3: 迭代法
    def longestPalindrome(self, s: str) -> str:
        # state: d[i][j] 表示s[i:j]是否是回文字符串
        # 0<=i<N; 0<=j<=N
        N = len(s)
        d = [[False]*(N+1) for _ in range(N)]

        # initial
        for i in range(N):
            d[i][i] = True
            d[i][i+1] = True

        # transition
        mx_len = 1
        ans = s[0] # 默认情况下填充单个字符 "a"，防止没进入循环；处理单个字符的情况
        for k in range(N-1): # 前面，列比行多1，初始化的时候，最后一行已经计算过了，所以还需要计算n-1行
            for i in range(N-k-1): # k=0，遍历N-1行
                j = i+k+2 # i=0, k=0, j=2，即j从2开始就行了，这个过程可以，代入特殊值来检验和判断
                d[i][j] = True if s[i]==s[j-1] and d[i+1][j-1] else False # 注意计算方式，当前d[i][j]依赖于左下角的d[i+1][j-1]
                if d[i][j] and mx_len < j-i:
                    ans = s[i:j]
                    mx_len = j-i
        return ans
    
    # method 2: 记忆化搜索——挂表法
    # AC
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1]*len(s) for i in range(len(s))]
        
        def dfs(s, l, r):
            # 增加缓存表，命中直接返回
            if dp[l][r] > -1:
                return dp[l][r] 

            ans = 0
            #未命中，展开
            if l == r:
                ans = 1
            elif l + 1 == r:
                ans = 1 if s[l] == s[r] else 0
            else:
                if s[l] == s[r]:
                    ans = dfs(s, l+1, r-1)
                else:
                    ans = 0
            #将计算结果加入缓存表，返回
            dp[l][r] = ans
            return dp[l][r] 


        mx = 0
        start, end = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(s, i, j) and j - i > mx:
                    start, end = i, j
                    mx = j - i

        return s[start:end+1]
    
    # method 1: MLE——记忆化搜索
    def longestPalindrome_1(self, s: str) -> str:
        # state: d[i][j] 表示s[i:j]是否是回文字符串
        # 0<=i<N; 0<=j<=N
        N = len(s)

        @cache
        def f(i, j):
            """表示s[i:j]是否是回文字符串"""
            # initial
            if i==j or i==j-1: return True # 空串
            if j==i+2: return s[i] == s[j-1]

            # transition
            return True if s[i] == s[j-1] and f(i+1, j-1) else False

        mx = 0
        ans = None
        for i in range(N):
            for j in range(i, N+1):
                if f(i, j):
                    if mx < j-i:
                        mx = j-i
                        ans = s[i:j]
        
        return ans

