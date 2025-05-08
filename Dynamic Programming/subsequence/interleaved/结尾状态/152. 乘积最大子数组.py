"""
[medium]

给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

 

示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 

提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何子数组的乘积都 保证 是一个 32-位 整数

https://leetcode.cn/problems/maximum-product-subarray/description/?envType=study-plan-v2&envId=top-100-liked

"""

"""
思路：
    1. 首先这是一个连续子序列问题 => 必然动态规划 => 且末尾状态
    2. 另外从时间复杂度而言，必然只有一个状态值 i
    3. 需要明白，最大值可能出现在哪里，要么是最大值，要么是负数乘以负数，因此需要两个状态数组

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # mx[i]表示以i结尾的连续子数组最大积
        # mn[i]最小乘积
        # 0<=i<N
        N = len(nums)

        mx = [_ for _ in nums]
        mn = [_ for _ in nums]

        for i in range(1, N):
            mx[i] = max(nums[i], nums[i]*mx[i-1], nums[i]*mn[i-1])
            mn[i] = min(nums[i], nums[i]*mx[i-1], nums[i]*mn[i-1])
        return max(mx + mn)