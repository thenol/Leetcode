"""
给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 < i < nums.length 。

重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。

 

示例 1：

输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
输出：3
解释：执行下述几个步骤：
- 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
- 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
- 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
[5,7,11,11] 是一个非递减数组，因此，返回 3 。
示例 2：

输入：nums = [4,5,7,7,13]
输出：0
解释：nums 已经是一个非递减数组，因此，返回 0 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109

"""
# https://leetcode.cn/problems/steps-to-make-array-non-decreasing/description/
# 思考过程：O(n)，因此可以逐个元素来计算被干掉的时间，找寻递推关系

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans = 0
        stk = []
        for num in nums:
            tick = 0
            # 当前元素一定是被它前面第一个比他大的元素干掉
            # 当前元素被干掉的时间为前一个比他小的元素被干掉的时间+1
            while stk and stk[-1][0] <= num: 
                tick = max(tick, stk.pop()[1])
            tick = tick + 1 if stk else 0 # 只有当前面确实有比它大的元素的时候，它才能被干掉，否则就不会被干掉啊！！！
            ans = max(ans, tick)
            stk.append((num, tick))
        
        return ans
                    
