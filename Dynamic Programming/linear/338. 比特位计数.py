"""
[easy]

给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

 

示例 1：

输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
示例 2：

输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

提示：

0 <= n <= 105
 

进阶：

很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）

https://leetcode.cn/problems/counting-bits/description/
"""

# 核心思路： O(N)
"""
从O(nlogn) 到 O(N) 自然想到，探索问题和子问题之间的关系，也就是当前数和之前数之间的关系
从而避免重复计算
"""

class Solution:
    def countBits(self, n: int) -> List[int]:   
        # state: d[i]表示i的1的个数
        d = [0]*(n+1)

        for i in range(1, n+1):
            if i % 2 == 0: # 偶数中1的个数和除以2的个数相同
                d[i] = d[i>>1]
            else: # 奇数中比前一个偶数多1个
                d[i] = d[i-1] + 1

        return d