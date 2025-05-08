"""
[medium]

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

 

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
 

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
 

进阶：

你能想出一个仅使用常数空间的一趟扫描算法吗？

https://leetcode.cn/problems/sort-colors/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
    1. 理解循环不变量
    2. 核心是用了 (l, p, r) 来成功的标识出了不同的区间，状态标识
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环不变量
        # [0, l)都是0
        # [l, p)都是1
        # [p, r)待确定
        # [r, n)都是2
        l, p, r = 0, 0, len(nums)

        while p < r:
            if nums[p] == 0:
                # 根据上面的循环不变量，nums[l] 是已确定区间的数，且 nums[l] == 1
                # 所以交换后 nums[p] == 1，需要 p += 1
                nums[p], nums[l] = nums[l], nums[p]
                l += 1
                p += 1 
            elif nums[p] == 1:
                p += 1
            else:
                # 根据上面的循环不变量，nums[r] 是待确定区间的数
                # 所以交换后 nums[p] 的值不一定为1，不需要 p += 1
                r -= 1
                nums[p], nums[r] = nums[r], nums[p]