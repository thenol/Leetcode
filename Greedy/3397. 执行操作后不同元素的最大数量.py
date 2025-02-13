"""
[medium]

给你一个整数数组 nums 和一个整数 k。

你可以对数组中的每个元素 最多 执行 一次 以下操作：

将一个在范围 [-k, k] 内的整数加到该元素上。
返回执行这些操作后，nums 中可能拥有的不同元素的 最大 数量。

 

示例 1：

输入： nums = [1,2,2,3,3,4], k = 2

输出： 6

解释：

对前四个元素执行操作，nums 变为 [-1, 0, 1, 2, 3, 4]，可以获得 6 个不同的元素。

示例 2：

输入： nums = [4,4,4,4], k = 1

输出： 3

解释：

对 nums[0] 加 -1，以及对 nums[1] 加 1，nums 变为 [3, 5, 4, 4]，可以获得 3 个不同的元素。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109

https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/description/
"""
from math import inf
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = -inf
        ans = 0
        for x in nums:
            x = min(max(pre+1, x-k), x+k) # 不能丢掉上届
            if pre < x:
                ans += 1
                pre = x
        
        return ans
        