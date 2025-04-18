"""
[medium]

如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

https://leetcode.cn/problems/arithmetic-slices/description/?source=vscode
"""

# 核心思路：连续子序列问题

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # state: d[i] 表示以i结尾的等差数列个数
        # 0<=i<N
        N = len(nums)
        d = [0] * N

        # initialization
        ...

        # transition
        for i in range(2, N): # 易错点❌： 2<=i，所以直接从第2个遍历就行了，看来❗️变量范围三步走❗️还是不能省略啊
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                d[i] = d[i-1] + 1 # 加上新增加的这个等差序列，也就是最后三个
        # print(d)
        return sum(d)

