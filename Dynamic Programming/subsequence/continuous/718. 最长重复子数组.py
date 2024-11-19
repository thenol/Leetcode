"""
[medium]

给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

 

示例 1：

输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。
示例 2：

输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/?source=vscode
"""

# 核心思路：两个序列上的 连续子序列问题
# 易错点❌：容易定义错状态，例如容易按照method 1去定义状态，即定义d[i][j]表示分别nums1[:i],nums2[:j] 范围 的最长公共子序列长度，但是这种 范围 状态定义，是没办法处理 连续子序列问题 的，

from functools import cache
class Solution:
    # method 3: 迭代版本
    # method 2: MLE
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # state: d[i][j] 表示以nums1[i],nums2[j]结尾的最长公共子序列长度
        # ❗️❗️❗️注意必须相邻
        # 0<=i<=N; 0<=j<=M
        N, M = len(nums1), len(nums2)
        d = [[0]*M for i in range(N)]
        # initialization
        # j==0
        for i in range(N):
            d[i][0] = nums1[i] == nums2[0] and 1
        # i==0
        for j in range(M):
            d[0][j] = nums1[0] == nums2[j] and 1

        # transition
        for i in range(1, N):
            for j in range(1, M):
                if nums1[i] == nums2[j]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = 0
        
        ans = 0
        # ❗️这一步，完全可以合并到上面的 transition 过程中的
        for i in range(N):
            for j in range(M):
               ans = max(ans, d[i][j]) 
        return ans


    # method 2: MLE
    def findLength_2(self, nums1: List[int], nums2: List[int]) -> int:
        # state: d[i][j] 表示以nums1[i],nums2[j]结尾的最长公共子序列长度
        # ❗️❗️❗️注意必须相邻
        # 0<=i<=N; 0<=j<=M
        N, M = len(nums1), len(nums2)

        @cache
        def f(i, j):
            """表示以nums1[i],nums2[j]结尾的最长公共子序列长度
            """
            nonlocal nums1, nums2
            if i<0 or j<0: return 0

            return f(i-1, j-1) + 1 if nums1[i] == nums2[j] else 0
        
        ans = 0
        for i in range(N):
            for j in range(M):
                ans = max(ans, f(i,j))
        
        return ans

    # method 1: 
    # ❌： WA, [0,1,1,1,1]\n[1,0,1,0,1]\n;
    # 正确：2；错误：3
    # 错误原因：
    #   还是在状态理解，d[i][j] 表示分别nums1[:i],nums2[:j]范围的最长公共子序列长度；
    #   当前 nums1[i-1] == nums2[j-1]，ans不一定为f(i-1, j-1) + 1，因为f(i-1, j-1)代表范围nums1[:i-1],nums2[:j-1]内的最长连续公共子序列，无法确保和当前是连续的，❗️❗️❗️注意必须相邻
    def findLength_1(self, nums1: List[int], nums2: List[int]) -> int:
        # state: d[i][j] 表示分别nums1[:i],nums2[:j]范围的最长公共子序列长度
        # 0<=i<=N; 0<=j<=M
        N, M = len(nums1), len(nums2)

        @cache
        def f(i, j):
            """表示分别nums1[:i],nums2[:j]范围的最长公共子序列长度
            """
            nonlocal nums1, nums2

            # initialization
            if i==0 or j == 0 : return 0 # 空数组

            # transition
            ans = 0
            if nums1[i-1] == nums2[j-1]:
                ans = f(i-1, j-1) + 1
            else:
                ans = max(f(i-1, j), f(i, j-1))
            
            return ans
        return f(N, M)
