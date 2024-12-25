"""
[hard]
对于一个整数数组 nums，逆序对是一对满足 0 <= i < j < nums.length 且 nums[i] > nums[j]的整数对 [i, j] 。

给你两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个 逆序对 的不同的数组的个数。由于答案可能很大，只需要返回对 109 + 7 取余的结果。

 

示例 1：

输入：n = 3, k = 0
输出：1
解释：
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2：

输入：n = 3, k = 1
输出：2
解释：
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
 

提示：

1 <= n <= 1000
0 <= k <= 1000

https://leetcode.cn/problems/k-inverse-pairs-array/description/?source=vscode
"""

# 核心思路：
"""
1. 能够看清增加一个n，能带来多少逆序对
2. 如何优化状态转移方程，降低时间复杂度
"""


from functools import cache

class Solution:
    # 优化状态转移方程
    # f(n, k) - f(n, k-1) = f(n-1, k) - f(n-1, k-n)
    def kInversePairs(self, n: int, k: int) -> int:
        # state: d[i][j] 表示前i个正数恰好组成k个逆序对的个数；
        # 0<=i<=n；0<=j<=k
        N = 10**9+7
        @cache
        def f(n, k):
            """表示前i个正数恰好组成k个逆序对的个数"""
            # initialization
            # 在递归
            if k == 0: return 1 # d[0][0] = 1
            if n == 0 or k < 0: return 0

            ans = 0
            # ans += f(n-1, k) # n不参与构建逆序对
            # n参与构建逆序对
            # 新增加1个数，可以在之前的基础上增加[1, n-1]种
            ans = f(n-1, k) - f(n-1, k-n) + f(n, k-1)
            
            return ans % N
        return f(n, k)

    # ❗️这不是01背包问题，数据范围为[1,n]全部都得选择
    #  method 2: 背包问题：01背包；
    # 结论：TLE 1000\n1000，O(N^3)
    def kInversePairs_2(self, n: int, k: int) -> int:
        # state: d[i][j] 表示前i个正数恰好组成k个逆序对的个数；
        # 0<=i<=n；0<=j<=k
        N = 10**9+7
        @cache
        def f(n, k):
            """表示前i个正数恰好组成k个逆序对的个数"""
            # initialization
            ...
            if k == 0: return 1
            if n == 0: return 0

            ans = 0
            # ans += f(n-1, k) # n不参与构建逆序对
            # n参与构建逆序对
            # 新增加1个数，可以在之前的基础上增加[1, n-1]种
            for j in range(n):
                if 0<= k-j: # 逆序对的个数必须为非负数
                    ans += f(n-1, k-j)
            
            return ans % N
        return f(n, k)
    
    # method 1: 区间dp；O(N^4)
    # def kInversePairs(self, n: int, k: int) -> int:
    #     # state: d[i][j] 表示前i个正数恰好组成k个逆序对的个数；
    #     # 0<=i<=n；0<=j<=k
    #     N = 10**9+7
    #     @cache 
    #     def f(n, k):
    #         """表示前i个正数恰好组成k个逆序对的个数；
    #         """
    #         nonlocal N
    #         if n-k<1:return 0
    #         if k == 0: return 1

    #         ans = 0
    #         for i in range(1, n+1):
    #             for j in range(1, k+1):
    #                 ans += f(i, j) + f(n-i, k-j)
            
    #         return ans % N
    #     return f(n, k)