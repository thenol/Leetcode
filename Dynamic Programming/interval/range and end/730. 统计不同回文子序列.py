"""
[hard]

给你一个字符串 s ，返回 s 中不同的非空回文子序列个数 。由于答案可能很大，请返回对 109 + 7 取余 的结果。

字符串的子序列可以经由字符串删除 0 个或多个字符获得。

如果一个序列与它反转后的序列一致，那么它是回文序列。

如果存在某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。

 

示例 1：

输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 是对 109 + 7 取余后的值。
 

提示：

1 <= s.length <= 1000
s[i] 仅包含 'a', 'b', 'c' 或 'd' 

https://leetcode.cn/problems/count-different-palindromic-subsequences/description/?source=vscode
"""

# 问题类型：
#   任意选择的随机字符序列
#   咋一看：字符串序列的解，无法通过序列上的字符的转移，向后传递，而要判断整体字符串是否时回文字符串，且统计数量，还要去重

# 核心思路：区间dp——端点和区间展开
#    1. 关注于，新增加的某个值，或者某两个端点值，给全局带来的增量
#    2. 正确的进行规模缩减，也就是找到转移方程之后，需要用特列法来验证是否正确


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # 初始化对角线，每个字符自身都是一个长度为1的回文子序列
        for i in range(n):
            dp[i][i] = 1
        
        # 动态规划填表
        for length in range(2, n + 1):  # 子串长度从2到n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    # 查找s[i]在s[i+1]到s[j-1]之间的位置
                    while low <= high and s[low] != s[i]:
                        low += 1
                    while low <= high and s[high] != s[i]:
                        high -= 1
                    if low > high:  # s[i]在s[i+1]到s[j-1]之间没有出现
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:  # s[i]在s[i+1]到s[j-1]之间出现一次
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:  # s[i]在s[i+1]到s[j-1]之间出现多次
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                
                dp[i][j] = (dp[i][j] + MOD) % MOD  # 确保结果非负
        
        return dp[0][n - 1]