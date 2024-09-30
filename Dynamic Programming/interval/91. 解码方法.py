"""
[medium]

一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

然而，在 解码 已编码的消息时，你意识到有许多不同的方式来解码，因为有些编码被包含在其它编码当中（"2" 和 "5" 与 "25"）。

例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1, 1, 10, 6)
"KJF" ，将消息分组为 (11, 10, 6)
消息不能分组为  (1, 11, 06) ，因为 "06" 不是一个合法编码（只有 "6" 是合法的）。
注意，可能存在无法解码的字符串。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。如果没有合法的方式解码整个字符串，返回 0。

题目数据保证答案肯定是一个 32 位 的整数。

 

示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
示例 3：

输入：s = "06"
输出：0
解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。
 

提示：

1 <= s.length <= 100
s 只包含数字，并且可能包含前导零。

https://leetcode.cn/problems/decode-ways/description/?source=vscode
"""

# 思路
"""
状态：d[i][j] 表示s[i:j]解码总数，符合题意，且可以表示题目所有含义
目标：d[0][len(s)]
范围：0<=i<len(s), i<=j<=len(s)
"""

# 易错点：
"""
1. 初始化:

"""

from string import ascii_uppercase
class Solution:
    def numDecodings(self, s: str) -> int:
        # state d[i][j] 表示s[i:j]解码总数
        # 0<=i<len(s), i<=j<=len(s)
        d = [[-1 for j in range(len(s)+1)] for i in range(len(s))]

        # preprocessing
        cnt = {
            str(k+1):v for k, v in enumerate(ascii_uppercase)
        }
        # print(cnt)

        # initialization
        # dependence: 0<=i, i<=j
        d[0][0] = 0
        for j in range(1, len(s)+1):
            #错误点： d[0][j] = 1 if s[0:j] in cnt else 0
            d[j-1][j] = 1 if s[j-1:j] in cnt else 0

        # print(d)    

        def f(s, i, j):
            """
            表示s[i:j]解码总数
            0<=i<len(s), i<=j<=len(s)
            依赖i,j,因此0<=i, i<=j<=len(s)
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            ans = 0
            # 整体可能性
            if s[i:j] in cnt:
                ans = 1
            for k in range(i, j): # [i+1, ..., j-1]
                if s[i:k] in cnt:
                    # 错误点： ans += f(s, i, k) * f(s, k, j)；错因：没有理解题目含义，题目的要求是必须前面和后面都能解码的情况下才算一种解码方式
                    ans += f(s, k, j) # 子集可能性，正确拆分可能性方法：聚焦其中首个字符，讨论它的可能性
            
            d[i][j] = ans
            return ans
        
        f(s, 0, len(s))
        # print(d)
        return d[0][len(s)]