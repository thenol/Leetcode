"""
[medium]

在一排多米诺骨牌中，tops[i] 和 bottoms[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）

我们可以旋转第 i 张多米诺，使得 tops[i] 和 bottoms[i] 的值交换。

返回能使 tops 中所有值或者 bottoms 中所有值都相同的最小旋转次数。

如果无法做到，返回 -1.

 

示例 1：


输入：tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
输出：2
解释： 
图一表示：在我们旋转之前， tops 和 bottoms 给出的多米诺牌。 
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。 
示例 2：

输入：tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
输出：-1
解释： 在这种情况下，不可能旋转多米诺牌使一行的值相等。
 

提示：

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6

https://leetcode.cn/problems/minimum-domino-rotations-for-equal-row/description/?source=vscode
"""

# 核心思路：
"""
聚焦最后一步决策：
必要条件：
    1. 需要[:i-1]上最小交换次数，或者最优解f()
    2. 将当前元素tops[i]，bottoms[i]进行合成某个数k

状态确定： d[i][j][k]，i范围变量，j顶部或者底部决策变量，k合成数的变量
转移方程：...
"""

from functools import cache 
from math import inf
class Solution:
    # method 1: 记忆化搜索
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # state: d[i][j][k] 表示[:i]范围内j=0顶部，1底部，可以合成全是k的最小翻转次数
        # 0<=i<=N; 0<=j<=1; 0<=k<=6
        N = len(tops)
        M = 2
        P = 7
        @cache 
        def f(i, j, k):
            """表示[:i]范围内j=0顶部，1底部，可以合成全是k的最小翻转次数"""
            nonlocal N, M, P

            # initialization
            # if i==0 or i==1: return 0 # 不需要翻转；❌：已经指定了k，单个元素需要判断是否和k相同啊，哎。。。为什么总是犯这种低级错误
            if i==0: return 0 # 不需要翻转

            # transition
            ans = inf
            if j == 0: # 合成top
                if tops[i-1] == k: # 不需要翻转
                    ans = min(ans, f(i-1, j, k))
                elif bottoms[i-1] == k: # 需要翻转1次
                    ans = min(ans, f(i-1, j, k)+1)
            elif j == 1: # 合成底部
                if bottoms[i-1] == k: # 需要翻转0次
                    ans = min(ans, f(i-1, j, k))
                elif tops[i-1] == k: # 需要翻转
                    ans = min(ans, f(i-1, j, k)+1)
            
            return ans

        ans = inf
        for j in range(2):
            for k in range(1, P):
                ans = min(ans, f(N, j, k))
        return ans if ans < inf else -1
     