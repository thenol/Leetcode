"""
[medium]

给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
 

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成

https://leetcode.cn/problems/longest-palindromic-subsequence/description/?source=vscode
"""

class Solution:
    # 迭代方式
    def longestPalindromeSubseq_1(self, s: str) -> int:
        # state: d[i][j] 表示s[i:j]是构成最长回文串
        # 0<=i<N; 0<=j<=N;
        # ❗️注意标定字符串s[i,...,j-1]
        N = len(s)
        d = [[0] * (N+1) for i in range(N)]        

        # initialization
        # 0<=i; 0<=j
        for i in range(N):
            d[i][i] = 0 # 空串
            d[i][i+1] = 1 # 只有一个字符

        # transition
        # i<N-1; 1<=j
        # d[i][j] = d[i+1][j-1] + 2 if s[i]==s[j]
        # d[i][j] = max(d[i+1][j], d[i][j-1]) else
        for k in range(N-1): # 最后一行已经初始化完成，只用算N-1次
            for i in range(N-1-k): # 当k=0，i只需遍历N-1行；检验i的范围满足条件
                j = i+k+2 # i=0, k=0, j直接从2开始计算
                if s[i] == s[j-1]:
                    d[i][j] = d[i+1][j-1] + 2 # 易错点❌：容易+1
                else:
                    d[i][j] = max(d[i+1][j], d[i][j-1])
        
        # print(d)
        return d[0][N]

    # 递归方式：
    def longestPalindromeSubseq(self, s: str) -> int:
        # state: d[i][j] 表示s[i:j]是构成最长回文串
        # 0<=i<N; 0<=j<=N
        N = len(s)

        @cache 
        def f(i, j):
            """表示s[i:j]是构成最长回文串"""
            nonlocal s
            if j-i == 1:
                return 1 # 只有一个字符
            if j-i == 0:
                return 0 # 空
            
            ans = 0
            if s[i] == s[j-1]:
                ans = f(i+1, j-1) + 2
            else:
                ans = max(f(i+1, j), f(i, j-1))
            
            return ans
        
        return f(0, N)