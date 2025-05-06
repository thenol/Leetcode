"""
[medium]

已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
示例 3：

输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
 

提示：

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked
"""


"""
后续题：33
思路：
    设 x=nums[mid] 是现在二分取到的数。

    我们需要判断 x 和数组最小值的位置关系，谁在左边，谁在右边？

    把 x 与最后一个数 nums[n−1] 比大小：

    如果 x>nums[n−1]，那么可以推出以下结论：
        nums 一定被分成左右两个递增段；
        第一段的所有元素均大于第二段的所有元素；
        x 在第一段。
        最小值在第二段。
        所以 x 一定在最小值的左边。
    
    如果 x≤nums[n−1]，那么 x 一定在第二段。（或者 nums 就是递增数组，此时只有一段。）
        x 要么是最小值，要么在最小值右边。
        所以，只需要比较 x 和 nums[n−1] 的大小关系，就间接地知道了 x 和数组最小值的位置关系，从而不断地缩小数组最小值所在位置的范围，二分找到数组最小值。


https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/1987499/by-endlesscheng-owgd/?envType=study-plan-v2&envId=top-100-liked
"""

# 开区间写法
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]


# 左闭右开区间写法
# 测试案例：[3,4,5,1,2]
# 循环不变量： 理解和维护循环不变量是写出正确二分查找代码的关键。循环不变量是在每次循环迭代前后都保持为真的条件，它可以帮助你理解算法的正确性。例如，在左闭右开区间查找中，循环不变量可以是“目标值如果存在，则一定在 [left, right) 区间内”。
class Solution:
    # 为什么正确：
    # 
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1 # hi = len(nums) - 1
        while l < h:
            m = (l+h)>>1
            if nums[m] < nums[-1]:
                h = m 
            else:
                l = m + 1
        return nums[l]
    
    # 思考为什么错
    # ❌：考虑分支 else，错在最后一个 nums[-1] 能取到时，这个时候如果 nums[m] == nums[-1]，那么会导致 l 越界
    # 纠正方法：
    #   1. 和 nums[0] 比较，从而两个分支都不会出错
    #   2. 将 h 初始化为 len(nums)-1
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) # hi = len(nums)
        while l < h:
            m = (l+h)>>1
            if nums[m] < nums[-1]:
                h = m 
            else:
                l = m + 1
        return nums[l]
    
    # 和 nums[0]比较
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)
        while l < h:
            m = (l+h)>>1
            if nums[m] < nums[0]:
                h = m
            else:
                l = m + 1
        return nums[l % len(nums)] if nums else -1
        

"""
好的，我们从理论的角度来解释为什么在左闭右开区间 [l, h) 的二分查找中，直接使用 nums[m] < nums[-1] 作为判断条件，可能会导致 l 或 h 越界。

左闭右开区间的性质：

    l 始终指向搜索区间的左边界，包含在搜索范围内。
    h 始终指向搜索区间的右边界，不包含在搜索范围内。
    循环在 l == h 时终止，此时搜索区间为空。
    有效的索引范围是 [0, len(nums) - 1].
分析 nums[m] < nums[-1] 的情况：

    假设我们使用左闭右开区间 [l, h) 和条件 nums[m] < nums[-1]。

    当 nums[m] < nums[-1] 时，我们执行 h = m。

    这看起来是安全的，因为 m 是当前搜索区间内的有效索引，并且更新 h 缩小了搜索范围。
    当 nums[m] >= nums[-1] 时，我们执行 l = m + 1。

    这里可能会出现问题。在循环结束时，l 和 h 会相等。如果最小值位于数组的后半部分，l 和 h 可能会收敛到 len(nums)。
    考虑一个具体的例子：[3, 4, 5, 1, 2]

    nums[-1] = 2

    初始 l = 0, h = 5

    迭代 1: m = 2, nums[2] = 5. 5 < 2 是 False，所以 l = 3. 区间变为 [3, 5).
    迭代 2: m = 4, nums[4] = 2. 2 < 2 是 False，所以 l = 5. 区间变为 [5, 5).
    循环终止，l == h == 5。
    如果我们在循环结束后返回 nums[l]，那么我们会尝试访问 nums[5]，这超出了数组的有效索引范围 (0 到 4)。

理论解释：

    当使用 nums[m] < nums[-1] 时，我们的目标是找到第一个小于 nums[-1] 的元素（或者最小值）。在左闭右开区间中，h 的含义是“第一个不满足条件的元素的索引”或者“搜索范围的结束”。

    在旋转数组的后半部分（包含最小值），元素通常小于数组的最后一个元素。当我们的搜索范围完全落在这个后半部分时，nums[m] 可能会一直小于 nums[-1]，导致 h 不断向左收缩。

    然而，当最小值是数组中最小的几个元素之一，并且位于数组的后半部分时，与 nums[-1] 的比较可能无法有效地将 l 推到最小值的位置。最终，l 可能会超越有效索引的末尾。

与 nums[0] 比较的优势（在左闭右开区间）：

    与 nums[0] 比较时，我们的目标是找到第一个小于 nums[0] 的元素（即旋转点，最小值）。在左半部分（大于等于 nums[0]），我们会移动 l。在右半部分（小于 nums[0]），我们会移动 h。当 l == h 时，它们会收敛到旋转点（最小值）的索引。由于 h 的初始值是 len(nums)，而 l 在移动时是 m + 1，因此最终 l 和 h 相等时，l 的值会是最小值的索引（在有效范围内）或者 len(nums)（如果数组是完全升序的）。因此，使用 l % len(nums) 可以更安全地处理边界情况。

总结：

直接使用 nums[m] < nums[-1] 在左闭右开区间下，由于 h 的含义以及 l 的更新方式，可能导致 l 在循环结束后超出数组的有效索引范围 [0, len(nums) - 1]。而与 nums[0] 比较，并结合左闭右开区间的特性，可以更稳定地将 l 或 h 收敛到最小值的索引。
"""