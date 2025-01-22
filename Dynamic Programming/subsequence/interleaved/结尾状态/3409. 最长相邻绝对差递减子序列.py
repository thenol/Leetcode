"""
[medium]

给你一个整数数组 nums 。

你的任务是找到 nums 中的 最长 
子序列
 seq ，这个子序列中相邻元素的 绝对差 构成一个 非递增 整数序列。换句话说，nums 中的序列 seq0, seq1, seq2, ..., seqm 满足 |seq1 - seq0| >= |seq2 - seq1| >= ... >= |seqm - seqm - 1| 。

请你返回这个子序列的长度。

 

示例 1：

输入：nums = [16,6,3]

输出：3

解释：

最长子序列是 [16, 6, 3] ，相邻绝对差值为 [10, 3] 。

示例 2：

输入：nums = [6,5,3,4,2,1]

输出：4

解释：

最长子序列是 [6, 4, 2, 1] ，相邻绝对差值为 [2, 2, 1] 。

示例 3：

输入：nums = [10,20,10,19,10,20]

输出：5

解释：

最长子序列是 [10, 20, 10, 19, 10] ，相邻绝对差值为 [10, 10, 9, 9] 。

 

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 300

https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/description/
"""

# 核心思路：
"""
思路总结：
    解的充要条件 <= 必然覆盖了所有子序列 <= 暴力遍历，组合数，肯定TLE <= 动态规划

    <= 状态数量选择 <= 从提示知道肯定是小于 O(n^2)的，且给出 nums[i] 的范围
    <= 初步判定状态表示为 f(i, j)，其中 0<=i<=len(nums), 1<=j<=max(nums)
    <= 状态含义：显然 i 表示范围，从题目中可以得出， 对于 nums[i] 需要知道和其之间的差，因此必然得知 j 表示 差值
    <= 状态转移方程： f(i, j) 可以从 f(idx[nums[i]+j], {j'| j<=j'}) 以及 f(idx[nums[i]-j], {j'| j<=j'}) 转移而来，这是题目条件，也是转移的必要条件
    <= 从这里知道 需要遍历 j' 的范围为 [0, max(nums)]，由此知道 时间复杂度为 O(nDD) = 10^4*300*300 = 10^8 显然还是不行
    <= 优化 需要简化 转移过程，仔细观察 f(idx[nums[i]+j], {j'| j<=j'}) 或者 f(idx[nums[i]-j], {j'| j<=j'}) 均为 遍历 D 求后缀最大值
    <= 缓存：直接用 f(i, j) 来缓存，即定义 f[i][j] 表示以 nums[i] 结尾的、最后两个数之差至少为 j 的子序列的最长长度，即：f(i, j) = max(f(i, {j'| j<=j'}))

最佳方法：
https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/solutions/3038930/zhuang-tai-she-ji-you-hua-pythonjavacgo-qy2bu/
"""

from functools import cache
class Solution:
    # def longestSubsequence(self, nums: List[int]) -> int:
    #     mx, mn = max(nums), min(nums)
    #     last = [-1] * (mx + 1)
    #     @cache
    #     def f(i, j):
    #         """表示以nums[i]结尾的，j<=j'的最长子序列"""
    #         if i==0 or j == mx-mn: return 0

    #         ans = 0
    #         ans = max(ans, f(i, j+1)) # j+1<=j'
    #         x = nums[i] - j
    #         if 0<=x and 0<=last[x]:
    #             ans = max(ans, f(last[x], j)+1)
    #         x = nums[i] + j
    #         if x<=mx and 0<=last[x]:
    #             ans = max(ans, f(last[x], j)+1)
            
    #         last[nums[i]] = i
    #         return ans

    #     for i in range(len())

    def longestSubsequence(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        max_D = mx - mn

        last = [-1] * (mx + 1)
        f = [[0] * (max_D + 2) for i in range(len(nums) )] # """表示以nums[i]结尾的，j<=j'的最长子序列，即后缀最大值"""
        for i, x in enumerate(nums):
            for j in range(max_D, -1, -1):
                f[i][j] = max(f[i][j+1], 1) # 很显然 max f(i, {j'| j+1<=j'}) <= max f(i, {j'| j<=j'}) 
                
                # 当差值正好为 j 时，如果存在继续更新最大值
                if x - j >= 0 and last[x - j] >= 0:
                    f[i][j] = max(f[i][j], f[last[x - j]][j] + 1)
                if x + j <= mx and last[x + j] >= 0:
                    f[i][j] = max(f[i][j], f[last[x + j]][j] + 1)
            last[x] = i
        return max(map(max, f))

if __name__ == "__main__":
    res = Solution().longestSubsequence(
        [6,5,3,4,2,1]
    )
    print(res)

        
