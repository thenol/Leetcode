"""
[medium]

给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

 

示例 1：

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
 

提示：

1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。

https://leetcode.cn/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0: # 规约态，是一个集合，划出了错误的边界，其他的情况下都有解
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(n - 1, m - 1)

    # ❌错在规约态，当i==0或者j==0的时候，答案可能为1
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache 
        def f(i, j): 
            # 分别以text1[i]和text2[j]结尾的最长公共子序列的长度
            if i<=0 or j<=0:return 0
            
            ans = 0
            if text1[i] == text2[j]:
                ans = max(ans, f(i-1, j-1) + 1)
            else:
                ans = max(ans, f(i, j-1), f(i-1, j))
            return ans
        return f(len(text1)-1, len(text2)-1)