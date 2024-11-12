"""
[medium]

给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

 

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

1 <= s.length <= 1000
s 由小写英文字母组成

https://leetcode.cn/problems/palindromic-substrings/description/?source=vscode
"""

# 核心思路：
# method 1: 区间dp；O(N^3)
# method 2: 中心扩展；O(N^2)

from functools import cache

class Solution:
    # method 1: O(N^3); O(N^2)枚举子串，O(N)时间检测是否是回文串
    def countSubstrings_1(self, s: str) -> int:
        # ✅state: d[i][j] 表示 s[i:j]是否是回文字符串
        # ❌state：注意如果直接定义d[i][j]为数量，无法进行规模缩减以及找到转移方程
        # 0<=i<j<=N
        N = len(s)
        @cache 
        def f(i, j, s):
            """表示 s[i:j]是否是回文字符串"""
            # initialization
            # 空串或者单个字符
            if j - i == 1 or i == j: return True
            # transition
            if s[i] == s[j-1]:
                return f(i+1, j-1, s)
            else: 
                return False

        ans = 0
        for i in range(N):
            for j in range(i+1, N+1):
                if f(i, j, s):
                    ans += 1
        
        return ans
    
    # method 2: O(N^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)  # 获取字符串的长度
        ans = 0  # 初始化回文子串的计数器

        # 遍历所有可能的中心点
        """
        为什么有 2 * len - 1 个中心点？ n + n-1 = 2*n-1
            aba 有5个中心点，分别是 a、b、c、ab、ba
            abba 有7个中心点，分别是 a、b、b、a、ab、bb、ba
        什么是中心点？
            中心点即 left 指针和 right 指针初始化指向的地方，可能是一个也可能是两个
        为什么不可能是三个或者更多？
            因为 3 个可以由 1 个扩展一次得到，4 个可以由两个扩展一次得到
        """
        for i in range(2 * n - 1):
            l = i // 2  # 计算左边界，对于奇数长度的回文子串，中心是单个字符
            r = l + i % 2  # 计算右边界，对于偶数长度的回文子串，中心是两个字符之间的位置

            # 在条件满足的情况下，扩展回文子串
            while l >= 0 and r < n and s[l] == s[r]:
                # 每找到一个回文子串，计数加一
                ans += 1
                # 向左和向右扩展
                l -= 1
                r += 1

        """
        假设字符串是 "abba"，长度 n = 4。
        执行流程：
            i=0, l=0, r=0, 单个字符, a
            i=1, l=0, r=1, 双字符, ab

            i=2, l=1, r=1, 单个字符, b
            i=3, l=1, r=2, 双字符, bb
            ...
        """

        # 返回回文子串的总数
        return ans
        