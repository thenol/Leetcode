"""
[medium]

给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
 

提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]

https://leetcode.cn/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：在可以选择的桥中，选择右端点最远的桥，它会让你走得更远
    
本质：贪心得选择能到达最远的 mx
    
注意：最后一个元素不用考虑，因为是要到达的元素，否则会多加一个，另外题目保证可以到达 nums[n-1]

https://leetcode.cn/problems/jump-game-ii/solutions/2926993/tu-jie-yi-zhang-tu-miao-dong-tiao-yue-yo-h2d4/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0  # 初始化跳跃次数
        cur_right = 0  # 当前能够到达的最远索引（当前桥的右端点）
        next_right = 0  # 从当前位置出发，下一步能够到达的最远索引（下一座桥的右端点的最大值）
        for i in range(len(nums) - 1):
            # 遍历数组，但不包括最后一个元素，因为我们的目标是到达最后一个元素
            # 在当前位置 i，我们能跳到的最远距离是 i + nums[i]
            # 我们不断更新 next_right，记录从当前桥的覆盖范围内，下一步能跳到的最远位置
            next_right = max(next_right, i + nums[i])
            # 如果当前遍历到的索引 i 等于当前能够到达的最远索引 cur_right，
            # 说明我们已经到达了当前桥的边缘，需要建造下一座桥；本质就是把这个范围里面所有的点都考虑了，能够到达的最远的 next_right
            if i == cur_right:
                # 更新当前能够到达的最远索引为下一步能够到达的最远索引
                cur_right = next_right
                # 跳跃次数加 1，表示建造了一座新的桥
                ans += 1
        # 返回总的跳跃次数，即建造的桥的数量
        return ans