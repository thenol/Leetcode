"""
[medium]

最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
Paste（粘贴）：粘贴 上一次 复制的字符。
给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。

 

示例 1：

输入：3
输出：3
解释：
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。
示例 2：

输入：n = 1
输出：0
 

提示：

1 <= n <= 1000

https://leetcode.cn/problems/2-keys-keyboard/description/?source=vscode
"""

# 核心思路：子序列问题——条件状态依赖
"""
思路的拆解：
两种出发方式：
思路1: 上来看决策变量只有1个，因此状态d[i]表示解，然后转移方程顺理成章
思路2: 思考"AAAAA"，可能从那些状态转移过来，"A", "AA",..., 因此很明显是最优子序列问题
"""

from math import inf
class Solution:
    def minSteps(self, n: int) -> int:
        # state: d[i] 表示 i个A所需要的最小操作数
        # 1<=i<=n
        d = [inf]*(n+1)
        if n == 1: return 0

        # initialization
        d[1] = 0

        # transition
        for i in range(1, n+1): # 最终求的A，起码不小于1个
            for j in range(1, i): # 纸上最开始有一个A
                if (i-j) % j == 0:
                    d[i] = min(d[i], d[j] + (i-j)//j + 1) # copy 1次，paste (i-j)//j次
        return d[n]