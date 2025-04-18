"""
[hard]

有 n 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次 移动 需要将 连续的 k 堆石头合并为一堆，而这次移动的成本为这 k 堆中石头的总数。

返回把所有石头合并成一堆的最低成本。如果无法合并成一堆，返回 -1 。

 

示例 1：

输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
示例 2：

输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
示例 3：

输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
 

提示：

n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30

https://leetcode.cn/problems/minimum-cost-to-merge-stones/description/?source=vscode
"""

from functools import cache
from itertools import accumulate
from math import inf
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        N = len(stones)
        if (N-1) % (k-1) !=0: return -1

        pre_s = list(accumulate(stones, initial=0))

        @cache
        def f(i, j, p):
            """区间[i,j)上合并p堆"""
            # if j-i<=p: return 0 # 等于p的时候，没有合并成本；归约态写法2
            if j-i==p: return 0 # 等于p的时候，没有合并成本；归约态写法1
            if p==1: return pre_s[j] - pre_s[i] + f(i, j, k) # 先合并成k堆，最后才能合并成1堆；注意为什么成本是 pre_s[j] - pre_s[i]，因为首先各个堆都已经分开堆到一起了，最后合成1堆的时候，就是所有的和，例如[a, b, c, d], k=2；则 [a+b, c+d] => [(a+b)+(c+d)]

            ans = inf
            # 从后往前
            for c in range(i+p-1, j, k-1):
                # 将[i,c)合并成一堆 (c-i) % (k-1) == 0
                ans = min(ans, f(i, c, p-1) + f(c, j, 1)) 
            
            # # 从前往后
            # for c in range(i+1, j, k-1): # ⭕️注意初始1个元素也算一堆
            #     # 将[i,c)合并成一堆 (c-i) % (k-1) == 0
            #     ans = min(ans, f(i, c, 1) + f(c, j, p-1))
            
            return ans
        return f(0, N, 1)

    # method 2: 区间dp
    def mergeStones(self, stones: List[int], k: int) -> int:
        # state: d[i][j] 表示stones[i:j]范围内合并的最低成本
        # 0<=i<N;0<=j<=N
        N = len(stones)
        pre_s = list(accumulate(stones, initial=0))

        @cache
        def f(i, j):
            """表示stones[i:j]范围内合并的最低成本"""
            nonlocal N, pre_s, stones
            
            # initialization
            if j-i==2: return pre_s[j]-pre_s[i]
            
            # transition
            ans = inf
            
            """
            1. ❌错误方式：

            # 这里有很多 错误❌ 的转移方式，放在这里供思考：
            
            ans = min(ans, stones[i] + f(i+1, j))
            ans = min(ans, pre_s[i+k]-pre_s[i] + f(i+k, j))

            # 这种展开方式的含义：i 要么和前k个数进行合并，要么和最后 f(i+1, j) 的数进行合并；
            # 很明显，这是❌错误的，比如 i 可能和 [i+1, j] 合并的某个中间态进行合并，而不一定非要和 [i+1,j] 合并完成的最终态进行合并，因此这种方式漏了很多情况。

            2. ✅正确方式思考：

            # 理论：状态的内涵或者必要条件，必须能够正确表示题目里面的所有关系、针对每一个元素时的决策，以及最终解
            # 思考：对于 stones[0] 有几种可能性？
            => stones[0]可能和后面 [i+1, j] 中的任何中间态进行合并，由解的完备性知，解必然覆盖这里所有的可能性；
            => 而状态的必要条件，必须能够正确表示所有关系，因此必须构造一种状态来表达所有关系和最终解
            => 


            
            """
            
            ans = 


    # method 1: 连续子序列合并问题，其中条件k为常量——子序列/范围
    # ❌：错在状态转换不能正确表达题目中的关系，题目中的要求是，合并之后，不会消失，而是以一个新的堆继续存在stones中。而以下的这种序列化建模的方式，可以表达的关系是当前元素cur是否单独累加或者和前一个元素一起累加，那么后面就不会再次加上这个累加值了，但是这是不对的，题意中表明，还可以继续相加
    def mergeStones_1(self, stones: List[int], k: int) -> int:
        # state: d[i] 表示stones[:i]范围内合并的最低成本
        # 0<=i<=N
        N = len(stones)
        pre_s = list(accumulate(stones, initial=0))
        d = [inf]*(N+1)

        # initialization
        d[0] = 0 # 空数组，返回0

        # transition
        for i in range(N+1):
            d[i] = d[i-1] # 单独合并
            if 0<=i-k:
                d[i] = min(d[i], d[i-k]+pre_s[i]-pre_s[i-k]) # ❌：d[i-k]+pre_s[i]-pre_s[i-k]表明[i-k,...,i-1]只能累加一次，与题意相悖
        return d[N]


"""
stones = [3, 2, 4, 1, 2, 3, 5]
k = 3

# 递归基：

                          dfs(0, 6, 1)
                             /         \
                  dfs(0, 2, 1)         dfs(3, 6, 1)
                    /    \                 /    \
           dfs(0, 0, 1) dfs(1, 2, 1)  dfs(3, 3, 1) dfs(4, 6, 1)
                                      /     \
                             dfs(4, 4, 1) dfs(5, 6, 1)


# 可以合并的证明：
 石头堆数: n
 每k个合成1堆
 
 可以合并证明：
 假设合并了 m 次，则有
 第1次合并完： n-(k-1)
 第2次合并完： n-2(k-1)
 ...
 第m次合并完： n-m(k-1)=1 最后还剩一堆
 
 因此： n-1 = m(k-1) => n-1 % k-1 == 0 充要条件


1. 问题的背景
题目要求将 stones 数组中的多个石块合并成一堆，每次合并 k 个连续的石块。合并的代价是合并的石块之和，我们希望计算将整个石块数组合并成一堆的最小代价。如果无法通过合并 k 个石块来最终合并成一堆，则返回 -1。

2. 分析问题结构
我们要解决的问题本质上是一个区间合并问题，涉及到多个子问题，且每个子问题的状态与以下因素有关：

当前考虑的区间：我们需要合并的石块位于数组的某个区间 [i, j] 中。
目标堆数：当前的目标是将区间 [i, j] 中的石块合并成 p 堆（p 是从 1 开始的）。
合并的成本：每次合并石块的成本是合并区间内石块的总和，我们需要确保能够在每个合并步骤中计算最小代价。

✅：最后一步，一定需要将所有的石头合并成k堆，这样才能最终合并成1堆
<= 需要以最小的代价，将区间合并成k堆
<= 枚举所有可能的合并方式，选择最低成本方式

3. 状态表示的选择
为了清楚地表示当前子问题的状态，我们需要以下信息：

区间 [i, j]：表示当前考虑的石块区间。
堆数 p：表示当前的目标是将区间 [i, j] 合并成 p 堆。
因此，我们定义 dp[i][j][p] 为：将区间 [i, j] 中的石块合并成 p 堆的最小成本。
"""