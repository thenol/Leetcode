"""
[medium]

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    # 时间复杂度：O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 先排序
        ans = []
        for i in range(len(nums)): # 遍历每一个 i，然后再继续寻找 左右两个指针
            if nums[i] > 0: # 如果最小元素已经大于0，则直接跳出
                return ans
            if i > 0 and nums[i] == nums[i - 1]: # 如果当前元素和前一个元素相同，跳过，避免重复
                continue
            l, r = i + 1, len(nums) - 1 # 双指针，开始搜索，此时必定 nums[i] < 0 且 nums[r] > 0；三数顺序：i -> l -> r；遍历主体为当前 i
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0: # 如果一组，则记录
                    ans.append([nums[i], nums[l], nums[r]]) 
                    while l < r and nums[l] == nums[l + 1]: # 如果当前 nums[l]重复，左指针一直右移，避免重复
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: # 如果当前 nums[r]重复，右指针一直左移，避免重复
                        r -= 1
                    l += 1 # 左指针右移一位
                    r -= 1 # 右指针右移一位
                elif nums[i] + nums[l] + nums[r] < 0: # 如果小于0，左指针右移
                    l += 1
                else: # 否则，右指针左移
                    r -= 1
        return ans