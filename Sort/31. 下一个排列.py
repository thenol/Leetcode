"""
[medium]

整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100

https://leetcode.cn/problems/next-permutation/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：

https://leetcode.cn/problems/next-permutation/solutions/3621022/jiao-ni-cong-ling-kai-shi-si-kao-zhe-ti-9qfrq/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        找到给定数字序列的下一个字典序排列。

        Args:
            nums: 一个整数列表，表示当前的排列。

        Returns:
            None: 直接修改输入的列表 nums，不返回任何值。
        """
        n = len(nums)

        # 第一步：从右向左找到第一个小于其右侧相邻数字的元素 nums[i]。
        # 这意味着从 nums[i+1] 开始的子数组是降序排列的。
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找到了这样的 nums[i]，则说明存在一个更大的字典序排列。
        if i >= 0:
            # 第二步：从右向左找到第一个大于 nums[i] 的元素 nums[j]。
            # 由于第一步中 [i+1:] 是降序的，所以找到的第一个大于 nums[i] 的元素就是右侧大于 nums[i] 的最小元素。
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]，使得在 i 这个位置放置一个更大的数字。
            nums[i], nums[j] = nums[j], nums[i]

        # 第三步：反转从 nums[i+1] 到数组末尾的子数组。
        # 在第二步交换之后，[i+1:] 这个子数组仍然是降序的（或者为空，如果 i 是最后一个元素的前一个）。
        # 为了得到下一个字典序排列，我们需要将这个子数组变成升序排列。
        # nums[i+1:] = nums[i+1:][::-1] 这种写法虽然简洁，但会创建新的列表，空间复杂度不是 O(1)。
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 如果第一步中没有找到 nums[i] (即 i < 0)，说明整个数组是降序排列的。
        # 此时，下一个字典序排列就是将整个数组反转成升序排列。
        # 第三步的反转操作在这种情况下同样适用，因为此时 left = 0, right = n - 1，会反转整个数组。
