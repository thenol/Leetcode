"""
[medium]

给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 
子数组
（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

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

https://leetcode.cn/problems/maximum-product-subarray/description/
"""

# 思路：
"""
由问题规模知，状态表示只能有一个变量，即 d[i]

状态表示：
    d[i] 表示以i为结尾的连续子数组最大值

转移方程：
    ...

初始化：
    ...

充要条件：
    乘积最大子数组 <=>  nums[i] * 连续子数组最大值或者最小值
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # state: d[i] 表示以i为结尾的连续子数组最大值
        dmax = [item for item in nums]
        dmin = [item for item in nums]
        for i in range(1, len(nums)):
            dmax[i] = max(dmax[i-1]*nums[i], nums[i], dmin[i-1]*nums[i])
            dmin[i] = min(dmax[i-1]*nums[i], nums[i], dmin[i-1]*nums[i])
        return max(dmax)