"""
[hard]

有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

 
示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
 

提示：

1 <= s.length <= 100
s 由小写英文字母组成

https://leetcode.cn/problems/strange-printer/description/?source=vscode
"""

# 核心思路：本质和[546]移除盒子完全相同，只是方向不同，一个是反向消除，一个是正向打印或者增加

from functools import cache
from itertools import groupby
class Solution:
    # method 2: 
    def strangePrinter(self, s: str) -> int:
        s = [a for a,b in groupby(s)]
        @cache
        def f(i,j):
            if i == j : return 0 
            return min(
                [f(i+1,j)+1] + 
                [f(i+1,k)+f(k,j) for k in range(i+1,j) if s[i]==s[k]]
            )
        return f(0,len(s))

    # method 1：
    def strangePrinter(self, s: str) -> int:
        g = [(a, len(list(b))) for a, b in groupby(s)]
        c, cnt = zip(*g)

        @cache
        def f(l, r, k): # ❗️其实k没用上，可以省略
            """[l, r)上前缀为k"""
            if l==r: return 0

            k += cnt[l]
            return min([f(l+1, r, 0) + 1] + [
                (f(l+1, i, 0) + f(i, r, k)) for i in range(l+1, r) if c[i] == c[l]
            ])

        return f(0, len(c), 0)