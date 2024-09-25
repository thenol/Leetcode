"""
[hard]

给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。

 
示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2：

输入：s = "aa", p = "*"
输出：true
解释：'*' 可以匹配任意字符串。
示例 3：

输入：s = "cb", p = "?a"
输出：false
解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
 

提示：

0 <= s.length, p.length <= 2000
s 仅由小写英文字母组成
p 仅由小写英文字母、'?' 或 '*' 组成

https://leetcode.cn/problems/wildcard-matching/description/?source=vscode
"""

# 最容易❌点：状态变量依赖的索引范围
# 边界初始化：由状态转移方程，可知 f(s, p, i, j) 依赖 i-1, j-1项，因此需要初始化 0 边界

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # state: d[i][j] s[:i], p[:j] 是否匹配
        #  0<=i<=len(s), 0<=j<=len(p)
        d = [[-1 for j in range(len(p)+1)] for i in range(len(s)+1)]

        # initialization
        d[0][0] = 1

        # p=''
        for i in range(1, len(s)+1):
            d[i][0] = 0
        # s=''
        for j in range(1, len(p)+1):
            d[0][j] = 0
            if p[j-1] == '*':
                d[0][j] = d[0][j-1]
        
        # print(d)
        
        def f(s, p, i, j):
            """
            s[:i], p[:j] 是否匹配
            0<=i<=len(s), 0<=j<=len(p)
            依赖 i-1, j-1，因此 i>=1, j>=1
            """
            if d[i][j] >= 0:
                return d[i][j]

            ans = 0
            if p[j-1] == '*':
                # 可以消耗一个，或者不消耗
                ans = f(s, p, i-1, j) or f(s, p, i-1, j-1) or f(s, p, i, j-1)
            elif p[j-1] == '?':
                ans = f(s, p, i-1, j-1)
            else:
                ans = f(s, p, i-1, j-1) if s[i-1] == p[j-1] else 0
            
            d[i][j] = ans
            return ans
        
        f(s, p, len(s), len(p))
        return bool(d[len(s)][len(p)])
