"""
[medium]

给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
 

提示：

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4

https://leetcode.cn/problems/delete-and-earn/description/?source=vscode
"""

# 最直观但走不通的错误思路：直观删除某个元素，及其 nums[i]-1，nums[i]，nums[i]+1，然后递归解决剩下子问题，但是难点在于无法表示删除后的数组，同时无法使用状态压缩，如果挨个删除，形成最后的数组，也无法使用cache

# 最佳思路：
"""
https://leetcode.cn/problems/delete-and-earn/solutions/758416/shan-chu-bing-huo-de-dian-shu-by-leetcod-x1pu/?source=vscode
"""

# 核心思路
"""
数据规模：1 <= nums[i] <= 10^4
因此可以直接离散化存储，开辟 total 数组，范围就开到 max_val + 1

转变成 打家劫舍题型，如果nums[i]被 删除1次，会让 所有的 nums[i]-1，nums[i]+1 全部删除，因此可以得到的收益为 nums[i] * c，其中 c 为nums[i]出现的次数

而结合开辟的 total 数组，得到当前状态 state 为到当前获得到的最大收益，当以 打家劫舍 的角度来计算时，当前的状态只能从 nums[i] - 2 转移而来，而 nums[i]+1显然无法转移得到，

总体而言：实现了在一个不大的数据规模下，将数据离散打平，从而能够直接转换成 排序好的 数组，因此自然转变成 打家劫舍 题型
"""

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        if N == 1: return nums[0]

        max_val = max(nums)
        total = [0] * (max_val + 1)
        for val in nums:
            total[val] += val
        
        before, last = total[0], max(total[0], total[1])
        for i in range(2, max_val+1):
            before, last = last, max(last, before + total[i])
        
        return last
