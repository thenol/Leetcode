"""
[hard]

给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。

设计一个算法使得这 k 个子数组各自和的最大值最小。

 

示例 1：

输入：nums = [7,2,5,10,8], k = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
示例 2：

输入：nums = [1,2,3,4,5], k = 2
输出：9
示例 3：

输入：nums = [1,4,4], k = 3
输出：4
 

提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

https://leetcode.cn/problems/split-array-largest-sum/description/?source=vscode
"""

import itertools
from functools import cache
from math import inf
# 切记✅：[左闭右开) 最好处理，且贴合语言特性
"""
最优解法：
https://leetcode.cn/problems/split-array-largest-sum/solutions/2613046/er-fen-da-an-fu-ti-dan-pythonjavacgojsru-n5la/?source=vscode

https://leetcode.cn/problems/split-array-largest-sum/solutions/21490/er-fen-cha-zhao-by-coder233-2/?source=vscode
"""
# ✅ 看到「最大化最小值」或者「最小化最大值」就要想到二分答案，这是一个固定的套路。

class Solution:
    # method 3: 二状态情况 + 二分
    def splitArray(self, nums: List[int], k: int) -> int:
        # 由于题目的返回要求：返回最小和的值
        # 最小和必然落在 [max(nums), sum(nums)] 之间
        # [max(nums), sum(nums)] 本质上对应 k=len(nums) 和 k=1
        # 我们可以使用二分来进行查找
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            # 淘汰算法
            # 我们由前向后对nums进行划分，使其子数组和 <= mid，然后统计满足条件的数组数量
            # 若我们选的sum值过小，则满足条件的数量 > m，目标值应落在 [mid+1, high]
            # 若我们选的sum值过大，则满足条件的数量 < m，目标值应落在 [low, mid-1]
            count = 0
            sub_sum = 0
            for i in range(len(nums)):
                sub_sum += nums[i] # sub_sum <= mid
                if sub_sum > mid: 
                    count += 1
                    sub_sum = nums[i] # 直接从nums[i]开始累积
            # 注意：末尾还有一个子数组我们没有统计，这里把它加上
            count += 1
            if count > k: # 子数组和<=mid的个数太多，应该减少切割点数，增大子数组和，即low 向 sum(nums) 移动
                low = mid + 1
            else: # count <= k；子数组和<=mid的个数太少，应该增大切割点数，减少子数组和，即high 向 max(nums) 移动
                high = mid
        return low # 算法的正确性证明：切分最大的时候，每个元素为一个区间；切分最小的时候，所有元素为一个区间，即原数组，因此必然存在一个  1<=k<len(nums)，使得切分成k的时候，最大连续子数组和 在 [max(nums), sum(nums)]之间；题设条件：0 <= nums[i] <= 10^6


    # method 2: 二状态情况 —— TLE, 
    def splitArray_2(self, nums: List[int], k: int) -> int:
        # state: d[i][k]表示在nums[:i]上划分成k个数组的；本质只枚举[0,i)，即第一个区间
        # 0<=i<=len(nums)；k
        N = len(nums)

        # initialization
        ...

        # preprocess
        pre_sum = list(itertools.accumulate(nums, initial=0))

        @cache
        def f(i, k):
            nonlocal pre_sum
            """
            表示在nums[:i]上划分成k个数组的；本质只枚举[0,i)，即第一个区间
            """
            if k == 1:
                return pre_sum[i] - pre_sum[0]
            
            ans = inf
            for g in range(i):
                prefix = pre_sum[i] - pre_sum[g] # 从后往前，枚举划分区间
                ans = min(ans, max(prefix, f(g, k-1)))
            return ans
        
        return f(N, k)
        

    # method 1: 三状态情况 —— TLE，
    def splitArray_1(self, nums: List[int], k: int) -> int:
        # state: d[i][j][k] 表示[i, j)上划分成k个数组各自和中最大值最小值；本质枚举了所有的i,j
        # 0<=i<j<=len(nums)+1
        N = len(nums)
        
        # initialization
        ...
        
        # preprocess
        # pre_sum[i]表示nums[:i]的累加和
        # 则 sum(nums[i:j]) = pre_sum[j] - pre_sum[i]
        # 0<=i<=N
        pre_sum = list(itertools.accumulate(nums, initial=0))
        # print(pre_sum)

        # transition
        @cache
        def f(i, j, k):
            """
            表示[i, j)上划分成k个数组各自和中最大值最小值
            条件：1<=k
            """
            if k == 1:
                return pre_sum[j] - pre_sum[i]
            
            ans = inf
            for g in range(i, j):
                prefix = pre_sum[g] - pre_sum[i] # [i, g)和f(g, j, k-1)，注意此时拆出一个固定的[i,g)，然后后面f(g, j, k-1)求出了[g, j)上所有可能拆分的和中最大的最小，而为了求得所有子数组和最大的最小，必须考虑连这前面[i,g)中取最大
                ans = min(ans, max(prefix, f(g, j, k-1)))
            return ans

        return f(0, N, k)