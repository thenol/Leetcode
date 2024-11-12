"""
[hard]

一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：

"AAJF" 对应分组 (1 1 10 6)
"KJF" 对应分组 (11 10 6)
注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。

除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息。

给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。

由于答案数目可能非常大，返回 109 + 7 的 模 。

 

示例 1：

输入：s = "*"
输出：9
解释：这一条编码消息可以表示 "1"、"2"、"3"、"4"、"5"、"6"、"7"、"8" 或 "9" 中的任意一条。
可以分别解码成字符串 "A"、"B"、"C"、"D"、"E"、"F"、"G"、"H" 和 "I" 。
因此，"*" 总共有 9 种解码方法。
示例 2：

输入：s = "1*"
输出：18
解释：这一条编码消息可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条。
每种消息都可以由 2 种方法解码（例如，"11" 可以解码成 "AA" 或 "K"）。
因此，"1*" 共有 9 * 2 = 18 种解码方法。
示例 3：

输入：s = "2*"
输出：15
解释：这一条编码消息可以表示 "21"、"22"、"23"、"24"、"25"、"26"、"27"、"28" 或 "29" 中的任意一条。
"21"、"22"、"23"、"24"、"25" 和 "26" 由 2 种解码方法，但 "27"、"28" 和 "29" 仅有 1 种解码方法。
因此，"2*" 共有 (6 * 2) + (3 * 1) = 12 + 3 = 15 种解码方法。
 

提示：

1 <= s.length <= 105
s[i] 是 0 - 9 中的一位数字或字符 '*'

https://leetcode.cn/problems/decode-ways-ii/description/?source=vscode
"""

# 核心思路：该讨论的一定需要讨论，别忘了，动态规划，只是以空间换时间，将暴力结果，通过空间缓存，所以一定是考虑了所有情况下的结果，也就是一定满足暴力情况下的解

from string import ascii_lowercase
from functools import cache
from unicodedata import digit
class Solution:
    # method 1: 分类讨论
    # 核心在于缩减规模的时候，如何处理单个字符和两个字符结尾的情况
    def numDecodings_1(self, s: str) -> int:
        # preprocess
        table = {str(k+1): c.upper() for k, c in enumerate(ascii_lowercase)}
        M = 10**9+7
        digits = [str(i) for i in range(1, 10)]

        # state: d[i]表示以i结尾的字符串的表示方法
        # 0<=i<len(s)
        N = len(s)
        
        @cache
        def f(i):
            """
            表示以i结尾的字符串的表示方法
            """
            nonlocal M, s, digits, table

            # initialization
            if i==0: # 初始化左边界
                if s[i] == "*": return 9
                return 1 if s[i] in table else 0
            if i<0:
                return 1 # 无字符串，此时递归访问的是空串，处理边界情况；这种情况是 默认末尾字符串 in table，此时算一种情况
            
            # transition
            ans = 0
            if s[i] == '*':
                # 单个字符结尾
                ans += 9 * f(i-1) 

                # 两个字符结尾
                if s[i-1] == '*':
                    ans += f(i-2) * 15
                else:
                    for c in digits:
                        ans += f(i-2) if s[i-1]+c in table else 0 
            else:
                # 单个字符结尾
                ans += f(i-1) if s[i] in table else 0 
                
                # 两个字符结尾
                if s[i-1] == "*":
                    for c in digits:
                        ans += f(i-2) if c+s[i] in table else 0 
                else:
                    ans += f(i-2) if s[i-1:i+1] in table else 0 
                
            return ans % M
        
        return f(N-1)
    
    # method 2: dp 迭代法——无哨兵法【区间：左闭右闭】
    def numDecodings_2(self, s: str) -> int:
        # preprocess
        table = {str(k+1): c.upper() for k, c in enumerate(ascii_lowercase)}
        M = 10**9+7
        digits = [str(i) for i in range(1, 10)]

        # state: d[i]表示以i结尾的字符串的表示方法个数
        # 0<=i<len(s)
        N = len(s)
        d = [0] * N

        # initialization
        # 2<=i
        if s[0] == "*": 
            d[0] = 9
        else:
            d[0] = 1 if s[0] in table else 0
        # ❗️❗️❗️讨论两个字符的情况, 很麻烦❗️❗️❗️
        """
        xxxx
        """

        
        # transition
        ans = 0
        for i in range(2, N):
            if s[i] == '*':
                # 单个字符结尾
                ans += 9 * d[i-1]

                # 两个字符结尾
                if s[i-1] == '*':
                    ans += d[i-2] * 15
                else:
                    for c in digits:
                        ans += d[i-2] if s[i-1]+c in table else 0 
            else:
                # 单个字符结尾
                ans += d[i-1] if s[i] in table else 0 
                
                # 两个字符结尾
                if s[i-1] == "*":
                    for c in digits:
                        ans += d[i-2] if c+s[i] in table else 0 
                else:
                    ans += d[i-2] if s[i-1:i+1] in table else 0 
            ans %= M

        return d[N-1]

    # method 3: 迭代法——有哨兵【区间：左闭右开】
    def numDecodings(self, s: str) -> int:
        # preprocess
        table = {str(k+1): c.upper() for k, c in enumerate(ascii_lowercase)}
        M = 10**9+7
        digits = [str(i) for i in range(1, 10)]

        # ✅state: d[i]表示s[:i]结尾的字符串的表示方法个数
        # 0<=i<=len(s)
        N = len(s)
        d = [0] * (N+1)

        # initialization
        # i==0：空串，默认在table里面
        d[0] = 1

        # i==1
        if s[0] == "*": 
            d[1] = 9
        else:
            d[1] = 1 if s[0] in table else 0
        
        # transition
        for i in range(2, N+1):
            ans = 0
            if s[i-1] == '*':
                # 单个字符结尾
                ans += 9 * d[i-1]

                # 两个字符结尾
                if s[i-2] == '*':
                    ans += d[i-2] * 15
                else:
                    for c in digits:
                        ans += d[i-2] if s[i-2]+c in table else 0 
            else:
                # 单个字符结尾
                ans += d[i-1] if s[i-1] in table else 0 

                # 两个字符结尾
                if s[i-2] == "*":
                    for c in digits:
                        ans += d[i-2] if c+s[i-1] in table else 0 
                else:
                    ans += d[i-2] if s[i-2:i] in table else 0 
            ans %= M
            d[i] = ans
        return d[N]