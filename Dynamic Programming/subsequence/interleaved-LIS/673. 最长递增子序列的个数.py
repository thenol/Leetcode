"""
[medium]

给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。

注意 这个数列必须是 严格 递增的。

 

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 

提示: 


1 <= nums.length <= 2000
-106 <= nums[i] <= 106

https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description/?source=vscode
"""

from math import inf
import bisect

# 核心需要解决两个问题：1）最长递增子序列长度是多少；2）求这种情况下最长递增子序列的个数
# 如何避免犯这种低级错误，反复尝试，发现最后方案不通的问题 ？
#   先提前演练一下，检验特列法，是否可以走通，再来编码
from collections import defaultdict
class Solution:
    # ✅：本质问题LIS上的双重dp
    # method 3：两个状态d[i],cnt[i]；
    # 前一个d[i]用来解决上述第一个问题，也就是最长递增子序列长度是多少
    # 后一个cnt[i]用来解决上述第二个问题，也就是统计递增子序列达到最大时，累计个数
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # state: d[i]表示以i结尾的最长严格递增子序列长度
        # cnt[i]所有以i结尾的最长严格递增子序列的个数
        # 0<=i<N
        N = len(nums)
        d = [1]*N
        cnt = [1]*N

        # initialization

        # transition
        for i in range(N):
            for j in range(i):
                if nums[j]<nums[i]:
                    le = d[j] + 1
                    if le == d[i]:
                        cnt[i] += cnt[j] 
                    elif d[i] < le:
                        cnt[i] = cnt[j]
                    d[i] = max(d[i], le)

        if max(d) == 1: return len(nums)
        mx_le, ans = 0, 0
        for i in range(N):
            if mx_le < d[i]:
                mx_le = d[i]
                ans = cnt[i]
            elif mx_le == d[i]:
                ans += cnt[i]

        return ans
                    
    
    
    # method 2: 通过d[i]来求
    # ❌ WA:
    """
    input: [1,2,4,3,5,4,7,2]
    实际最长序列长度为5，为一下序列：
    [1, 2, 4, 5, 7]
    [1, 2, 3, 5, 7]
    [1, 2, 3, 4, 7]

    错因：通过这种方式，只能累积到1个，具体过程如下：
    
    当计算到7时
    le, nums[j], mx_le, ans
    2 1 4 3
    3 2 4 3
    4 4 4 4
    4 3 4 5
    5 5 5 1 # 发现了5, 7的序列，但是5，7的序列实际有2个
    5 4 5 2 # 发现了4, 7的序列
    5 2 [1, 2, 3, 3, 4, 4, 5, 2]
    """
    def findNumberOfLIS_2(self, nums: List[int]) -> int:
        # state: d[i] 表示以i结尾的最长递增子序列长度
        # 0<=i<N
        N = len(nums)
        d = [1] * N

        # initialization
        mx_le = 1
        ans = 0

        # transition
        for i in range(N):
            for j in range(i):
                if nums[j]<nums[i]: # 计算以i结尾的所有严格递增子序列的长度
                    le = d[j]+1
                    d[i] = max(d[i], le)
                    if mx_le < le:
                        mx_le = le
                        ans = 1
                    elif mx_le == le:
                        ans += 1
                    if nums[i] == 7:
                        print(le, nums[j], mx_le, ans)
            if mx_le == 1: # 没找到，统计长度为1的个数
                ans += 1
        print(mx_le, ans, d)
        return ans

    # method 1: 通过tails来求
    # ❌ WA：原因，虽然t的下标保存了最长递增子序列的长度信息，但是无法统计数量
    # 这种解法只能解决判断 “是否存在问题”：  以i结尾的最长递增子序列的长度问题
    # 原因是算法的核心思想是每次以贪心的保存所有最长子序列的末尾的最小值，然后方便后面尽可能得形成最长递增子序列
    # 这种贪心的过程，已经丢失了中间那些个数
    # ❗️❗️❗️一种想法是：通过长度为3的个数 x 长度为4的个数，但是其实这是错误的，因为长度为3的所有子序列，不一定都能和长度为4的末尾形成长度为4的递增子序列
    # 无法计算以i结尾的最长递增子序列 “有多少个问题” 
    def findNumberOfLIS_1(self, nums: List[int]) -> int:
        # state: tail[i] 表示子序列长度为i+1的所有序列的最小值
        # 0<=i<N
        N = len(nums)
        t = [inf] * N
        le = [0] * N # 记录队列个数

        # initialization

        # transition
        for i in range(N):
            k = bisect.bisect_left(t, nums[i]) # 贪心得寻找最长子序列
            t[k] = min(t[k], nums[i])
            le[k] += 1

        print(le)
        for i in range(N-1, -1, -1):
            if 0<le[i]:
                return le[i]
        