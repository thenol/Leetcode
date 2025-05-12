'''
[medium]

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        给定一个包含 n + 1 个整数的数组 nums，每个整数都在 [1, n] 范围内（包括端点），
        数组中恰好存在一个重复的数字。找出这个重复的数字。

        这个算法使用 Floyd 的龟兔赛跑算法（也称为循环检测算法）来解决这个问题。
        我们将数组看作一个链表，其中 nums[i] 表示索引 i 的下一个节点。
        由于存在重复的数字，所以这个链表中必然存在环。

        Args:
            nums: 一个包含 n + 1 个整数的列表，每个整数都在 [1, n] 范围内，且包含一个重复数字。

        Returns:
            int: 数组中重复的那个数字。
        """
        # 初始化快慢两个指针，都指向数组的起始位置（索引 0）。
        fast = slow = 0

        # 第一阶段：找到快慢指针的相遇点。
        # 快指针每次移动两步，慢指针每次移动一步。
        # 由于存在环，它们最终会在环内的某个节点相遇。
        fast = nums[nums[fast]]
        slow = nums[slow] # ⭕️先移动一次，确保快指针和慢指针不在同一位置，即进入不了下面循环语句
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        # 第二阶段：找到环的入口，即重复的数字。
        # 将快指针重新指向数组的起始位置。
        # 保持慢指针在相遇点。
        # 这次，快慢指针都每次移动一步。
        # 当它们再次相遇时，相遇的节点就是环的入口，也就是重复的数字。
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        # 返回相遇点的值，即重复的数字。
        return fast