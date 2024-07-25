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

记忆化搜索步骤：
1. 增加缓存表，命中直接返回
2. 未命中，展开
3. 将计算结果加入缓存表，返回

"""

class Solution:
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


# Method two: 填表法
"""
填表法（迭代表）步骤
1. 特例法，先特例画出 n 比较小的格子，类似于数独
2. 按照填格子的步骤，写出代码
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        d=[[-1 for _ in range(N)] for _ in range(N)]
        mx=0
        start=end=0
        for le in range(1,N+1): #控制遍历次数，执行N次
            for i in range(N-le+1): # 控制遍历行，次序为[0,N), [0,N-1), [0,N-2),..., [0,1), 同样是 N 次
                j=i+le-1 # 控制遍历列，每次遍历，列都会右移一个，第le次遍历，自然右移le，但是 j 得从i位置开始，因此自然得初始为 i+le-1 (否则j就从i右边第一个下标开始了)
                d[i][j]=s[i]==s[j] and ( le < 3  or d[i+1][j-1]) # 极其简洁的表达：控制前两次边界填充，当大于等于3时，开始采用状态转移方程
                if d[i][j] and j-i>mx:
                    start,end=i,j
        return s[start:end+1]

"""
# 极其精简的表达
d[i][j]=s[i]==s[j] and ( le < 3  or d[i+1][j-1])

# 展开
if le < 3:
    d[i][j]=s[i]==s[j]
else:
    d[i][j]=s[i]==s[j] and d[i+1][j-1]

"""
            



       