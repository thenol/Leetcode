"""
[meidum]

给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同

https://leetcode.cn/problems/largest-divisible-subset/description/?source=vscode
"""

# 思路：本质最长递增子序列问题
# 核心思路：1）将问题简化为 大数 % 小数 == 0 问题；2）此外，对于 nums[i]<=nums[j]<= nums[k]，如果 nums[i] in s[nums[j]]，且 nums[k] % nums[j] == 0，则s[nums[k]]=s[nums[j]]且 nums[i]一定在 s[nums[k]]中

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # s[nums[i]] 表示能整除nums[i]的整数集合
        nums = sorted(nums)
        N = len(nums)

        # initialization
        s = {k:[] for k in nums}

        # transition
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(s[nums[i]]) < len(s[nums[j]]) + 1:
                    s[nums[i]] = s[nums[j]] + [nums[j]]
                # print(s)
        mx = 0
        ans = None
        for k, v in s.items():
            if mx < len(v):
                ans = v + [k]
                mx = len(v)
        return ans if ans else nums[:1]
