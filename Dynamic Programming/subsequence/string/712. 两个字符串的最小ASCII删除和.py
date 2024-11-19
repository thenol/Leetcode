"""
[medium]

给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。

 

示例 1:

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
示例 2:

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
 

提示:

0 <= s1.length, s2.length <= 1000
s1 和 s2 由小写英文字母组成

https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/description/?source=vscode
"""

# 核心思路：串上问题
# 易错点：初始化
# 避免初始化错误的方式：特列检查法，就是带入特例，然后按照代码计算出来，看看值是否符合预期

from math import inf
from functools import cache
from string import ascii_lowercase
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # state: d[i][j]表示s1[:i], s2[:j]两个字符串相等所需删除字符的 ASCII 值的最小和 。
        # 0<=i<=N; 0<=j<=M
        N, M = len(s1), len(s2)

        @cache
        def f(i, j):
            """表示s1[:i], s2[:j]两个字符串相等所需删除字符的 ASCII 值的最小和 """

            # initialization
            if i==0 and j == 0: return 0
            # 易错点❌：再次卡在了初始化这里，错误地计算成了整个s1和s2
            if i==0: return sum([ord(c) for c in s2[:j]])
            if j==0: return sum([ord(c) for c in s1[:i]])

            # transition
            ans = inf

            ## 方式1:
            if s1[i-1] == s2[j-1]:
                ans = min(f(i-1, j-1), ans)
            else:
                ans = min(ans, f(i-1, j) + ord(s1[i-1]), f(i, j-1) + ord(s2[j-1]))

            ## 方式2: 相比方式1，多计算了
            # ans = min(ans, f(i-1, j)+ord(s1[i-1])) # 删s1[i-1]
            # ans = min(ans, f(i-1, j-1)+ord(s1[i-1])+ ord(s2[j-1])) # 删s1[i-1] 和 s2[j-1]

            # ans = min(ans, f(i, j-1) + ord(s2[j-1])) # 删s2[j-1]

            # if s1[i-1] == s2[j-1]:
            #     ans = min(ans, f(i-1, j-1)) # 相等抵消
            
            return ans
        
        return f(N, M)
