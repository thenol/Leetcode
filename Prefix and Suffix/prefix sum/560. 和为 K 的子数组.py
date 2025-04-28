"""
[medium]

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0 # 初始化
        cnt = defaultdict(int) # 记录各种子序列和出现对次数；注意所有为出现在 cnt 中对值都默认为 0
        cnt[0] = 1  # s[0]=0 单独统计；0默认出现1次；⭕️易错点，别忘了初始化
        for x in nums:
            s += x # 累计前缀和
            ans += cnt[s - k] # 直接判断是否存在前缀和为 s-k；本质 当前前缀和为 s，如果存在 某个前缀和为 t，满足 s-t=k，则 s-k 的前缀和一定存在
            cnt[s] += 1 # 继续记录前缀和
        return ans
