"""
[medium]

给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

 

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
示例 2:

输入: nums = [1,2,3,4], k = 3
输出: false
 

提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
每个元素的频率在 [1,4] 范围内

https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/?source=vscode
"""

# 核心思路：暴力回溯 + 状态压缩
# 易错点：初始化条件

from functools import cache
class Solution:
    # method 1: 状态压缩dp 
    # 问题特征：随机选择、随机组合
    # 相比于直接用list回溯遍历的有点，可cache
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # state: d[mask][k][v]表示用mask的数能否构建第k个子集合，当前第k个子集合还剩v大小
        # 0<=mask<=2^16-1; 1=<k<=K; 0<=v<=V
        N = len(nums)
        s = sum(nums)
        if s % k != 0: return False
        V = s // k

        @cache
        def f(mask, k, v):
            """表示用mask的数能否构建k个相等的
            """
            nonlocal N, nums, V
            # print(bin(mask), k, v)

            # initialization
            # 0<=mask<=2^16-1; 1=<k<=K; 0<=v<=V
            if v<0 or k<0: return False
            
            # ✅：想想最平凡的情况下，初始化条件是什么
            if v==V and k == 0 and mask == 0: return True

            # 0<v and 0<k and mask !=0
            # transition
            ans = False
            for i in range(N):
                if (mask >> i) & 1:
                    leave = v - nums[i]
                    if leave == 0:
                        ans = ans or f(mask ^ (1<<i), k-1, V)
                    else:
                        ans = ans or f(mask ^ (1<<i), k, leave)
            
            return ans

        return f((1<<N)-1, k, V)
        