"""
[hard]

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是
回文串
。

返回符合要求的 最少分割次数 。

 

示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1
 

提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成

https://leetcode.cn/problems/palindrome-partitioning-ii/description/
"""

# 思路：
"""
总体思路：1. 预处理判断是否是回文串；2.求取切割最小次数

【方法一】
状态表示：
    d[i][j] 表示 s[i:j]需要的最小分割次数

状态转移方程
    ...

状态初始化：
    ... 见代码

结果：
    TLE ❌

原因：
    数据范围 1 <= s.length <= 2000，如果用d[i][j] 表示状态，再遍历分割点 k, 时间复杂度 O^3，即10^9，超时

【方法二】
状态表示
    g[i] 表示 s[:i] 需要的最小分割次数

转移方程
    ...

状态初始化
    ...

易错点❌
    最容易犯错，用贪心算法，但是这里贪心出的结果可能是局部最优，而不是全局最优

"""


from math import inf
class Solution:
    def minCut(self, s: str) -> int:

        ## 回文串判断
        # state 2: c[i][j] 表示 s[i:j] 是否是回文串
        # 0<=i<len(s), 0=j<=len(s)
        c = [[-1 for j in range(len(s)+1)] for i in range(len(s))]
        # initialization
        for i in range(len(s)):
            c[i][i] = 1
            c[i][i+1] = 1
            # 这里已经初始化了 j-i<=1情况

        def f1(i, j):
            """
            c[i][j] 表示 s[i:j] 是否是回文串
            0<=i<j<=len(s)
            依赖：
            1<=j, 0<=i
            """
            # 由初始化知，j-i<=1的情况，直接返回
            if c[i][j] >=0:
                return c[i][j]
            
            # j-i>=2的情况继续执行，正好满足条件 j>=i+2
            ans = 0
            if s[i] == s[j-1]:
                ans = f1(i+1, j-1) # j-1>=i+1 => j>=i+2
            
            c[i][j] = ans
            return ans
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                f1(i,j)

        ## 求最小分割次数
        ### method 1:
        # state 1: d[i][j] 表示 s[i:j]需要的最小分割次数
        # 0<=i<=j<=len(s)
        d = [[-1 for j in range(len(s)+1)] for i in range(len(s))]

        # initialization
        for i in range(len(s)):
            d[i][i] = 0
            d[i][i+1] = 0

        # transition
        def f2(i, j):
            """
            d[i][j] 表示 s[i:j]需要的最小分割次数, 0<=i<=j<=len(s)
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            ans = inf
            if c[i][j] == 1:
                ans = 0
            else:
                for k in range(i+1, j):
                    tmp = f2(i, k) + f2(k, j) + 1
                    ans = min(tmp, ans)
            
            d[i][j] = ans
            # if i==0 and j==3:
            #     print(ans, c[i][j], c[i+1][j], f(0,1), f(1,3))
            return d[i][j]
        
        # f2(0, len(s)) # TLE
        # print(d)
        # return d[0][len(s)]

        ### method 2:
        # state: g[i] 表示 s[0:i+1]最小分割次数, 0<=i<=len(s)
        g = [-1 for i in range(len(s)+1)]
        n = len(s)

        # intialization
        g[0] = 0

        # transition
        def f3(i):
            """
            g[i] 表示 s[:i]最小风格次数, 0<=i<=len(s)，注意i不包含在处理的字符串中
            依赖：
            1<=i
            """
            if g[i] >= 0:
                return g[i]

            ans = inf
            ## 错误❌写法，这不是正确的可能性拆分。核心原因：贪心不一定是全局最优
            # for j in range(i-2, -1, -1):
            #     if c[j][i] == 1:
            #         # 贪心策略，如果s[:i]后缀是回文串，则继续向前
            #         continue
            #     else:
            #         # 不是回文串，做一次分割
            #         ans = f3(j+1) + 1
            
            ## 正确可能性分割：需要对比所有割出来的回文串中的最小分割次数
            if c[0][i] == 1:
                ans = 0
            else:
                for j in range(0,i):
                    # print(j, i, c[j][i])
                    if c[j][i] == 1:
                        # 易错点❌：找到最长 s[j:i]为回文串,但是这种分割方法不一定最优, 例如 "abbab"
                        # 最后一个字符 c[j][i] === 1 恒成立
                        ans = min(ans, f3(j) + 1)

            g[i] = ans
            return g[i]

        f3(len(s))
        return g[len(s)]
