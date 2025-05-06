"""
[medium]

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

https://leetcode.cn/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思考：
    1. 前序题：153. 寻找旋转排序数组中的最小值.py


https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/1987503/by-endlesscheng-auuh/?envType=study-plan-v2&envId=top-100-liked
"""


class Solution:
    # 153. 寻找旋转排序数组中的最小值（返回的是下标）
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return right

    # 有序数组中找 target 的下标
    def lower_bound(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            # 循环不变量：
            # nums[right] >= target
            # nums[left] < target
            if nums[mid] >= target:
                right = mid  # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        return right if nums[right] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        if target > nums[-1]:  # target 在第一段
            return self.lower_bound(nums, -1, i, target)  # 开区间 (-1, i)
        # target 在第二段
        return self.lower_bound(nums, i - 1, len(nums), target)  # 开区间 (i-1, n)


# TLE
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1 
        while left < right:  # 
            mid = (left + right) >> 1
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid+1
        return left

    def lower_bound(self, nums, s, e, target):
        l, h = s, e
        x = target - 1
        while l < h:
            m = l + (h-l)>>1
            if x < nums[m]:
                h = m
            else:
                l = m + 1
        return l if l <= e and nums[l] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        mn = self.findMin(nums)
        if nums[-1] < target:
            s, e = 0, mn # 第一段
        else:
            s, e = mn, len(nums) # 第二段
        
        ans = self.lower_bound(nums, s, e, target)
        return ans 
        
        