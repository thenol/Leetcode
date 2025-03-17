"""
[medium] 

给你一个整数数组 nums 和一个正整数 k，返回所有长度最多为 k 的 子序列 中 最大值 与 最小值 之和的总和。

非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。

由于答案可能非常大，请返回对 109 + 7 取余数的结果。

 

示例 1：

输入： nums = [1,2,3], k = 2

输出： 24

解释：

数组 nums 中所有长度最多为 2 的子序列如下：

子序列	最小值	最大值	和
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
总和	 	 	24
因此，输出为 24。

示例 2：

输入： nums = [5,0,6], k = 1

输出： 22

解释：

对于长度恰好为 1 的子序列，最小值和最大值均为元素本身。因此，总和为 5 + 5 + 0 + 0 + 6 + 6 = 22。

示例 3：

输入： nums = [1,1,1], k = 2

输出： 12

解释：

子序列 [1, 1] 和 [1] 各出现 3 次。对于所有这些子序列，最小值和最大值均为 1。因此，总和为 12。

 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= min(100, nums.length)

https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/description/?slug=sum-of-variable-length-subarrays&region=local_v2
"""

"""
核心思路：
    * 【推理过程】
        <= 解一定覆盖所有的可能性
        <= 问题两个关键：1. 可变子序列 2. 最大值与最小值之和
        <= 由解的必要条件知道，一定覆盖所有序列，且每个序列的最大值与最小值之和
        <= 直观思路：1. 暴力遍历，铁定超时；2. 动态规划，找到最优子结构，但是不好找，没见过这种模板类型
        <= 由提示知道，时间复杂度范围为 O(n) ~ O(NlogN)
    * 【条件转化】
        <= 由于排序不影响最大值和最小值之和，所以可以先排序
        <= 最大值和最小值之和 转化为 分别求最大值和最小值，且针对每个元素，求最大值和最小值
        <= 子序列 变为 贡献法
        <= 求最大最小值，采用组合数学 + 贡献法
    * 【归纳总结】
        * 贡献法 + 组合数学

最佳实践：https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/solutions/3051549/gong-xian-fa-zu-he-shu-xue-pythonjavacgo-0jod/?slug=sum-of-variable-length-subarrays&region=local_v2
"""

# 更快的写法见【预处理】
from math import comb
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        nums.sort()
        ans = 0
        s = 1
        for i, x in enumerate(nums):
            # 根据对称性，nums[n−1−i] 作为最小值时，子序列个数和 nums[i] 作为最大值的个数是一样的，所以二者可以一同计算。
            # 本质上是因为，区间长度相同， 即[0,...,i] 与 [n-1-i,...,n-1]，都有i+1个元素，所以组合数学的组合数是一样的
            ans += (x + nums[-1 - i]) * s 
            s = (s * 2 - comb(i, k - 1)) % MOD # 之所以为 k-1，是因为，贡献法默认包含了自身；
        return ans % MOD
