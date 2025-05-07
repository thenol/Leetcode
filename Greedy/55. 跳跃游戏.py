"""
[medium]

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 104
0 <= nums[i] <= 105

https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
https://leetcode.cn/problems/jump-game/solutions/2798996/liang-chong-li-jie-fang-shi-wei-hu-zui-y-q67s/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    # O(N)
    def canJump(self, nums: List[int]) -> bool:
        mx = 0  # 初始化最远可以到达的索引
        for i, jump in enumerate(nums):
            # 遍历数组中的每个位置和该位置可以跳跃的最大步数
            if i > mx:
                # 如果当前索引 i 超过了之前可以到达的最远索引 mx，
                # 说明无法到达当前位置，因此返回 False
                return False
            mx = max(mx, i + jump)
            # 更新最远可以到达的索引：当前最远索引 mx 和从当前位置 i
            # 可以跳到的最远索引 (i + jump) 中取较大值
            if mx >= len(nums) - 1:
                # 如果最远可以到达的索引 mx 已经大于或等于数组的最后一个索引，
                # 说明可以跳到数组的末尾，返回 True
                return True
        # 如果循环遍历结束都没有返回 True，说明无法跳到数组末尾，返回 False
        return False
    
    # ❌ TLE; O(n*max(nums))
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def f(i):
            if i == n-1:
                return True
            
            ans = False
            for j in range(1, nums[i]+1):
                ans = ans or f(i+j)
            return ans
        
        return f(0)