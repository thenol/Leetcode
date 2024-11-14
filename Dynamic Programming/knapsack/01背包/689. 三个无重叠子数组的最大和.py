"""
[hard]

给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

 

示例 1：

输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
示例 2：

输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)

https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/description/?source=vscode
"""

# 核心考点：前缀和预处理+01背包+查找背包中哪些被放入背包

from itertools import accumulate
from operator import sub
class Solution:
    # method 2: 哨兵——左右护法
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        # step 1: 先求解nums中以nums[i]结尾的子序列长度为k的序列和
        # preprocess
        # pre_sum[i]表示nums[:i]的和
        # 0<=i<=N
        pre_sum = list(accumulate(nums, initial=0))
        
        sub_sum = [0]*(N+1) # sub_sum[i]表示以nums[i-1]为结尾的连续长度为k的子序列和
        for i in range(N+1):
            # 第一个k个元素子序列[0, k)
            if 0 <= i-k:
                sub_sum[i] = pre_sum[i] - pre_sum[i-k]
        
        # step 2: 开始条件背包
        # state: d[i][j]表示在sub_sum上前[0,i-1]范围内选取j个元素的最大值，且要求j个元素之间间隔为k
        # 0<=i<=N; 0<=j<=3
        Q = 3
        d = [[0]*(Q+1) for i in range(N+1)]
        record = [[False]*(Q+1) for i in range(N+1)] # 用来记录背包容量为j的时候，i有没有被选择

        # initialization
        # 0<=i<N, 1<=i, k<=i; 0<=j<=3,1<=j
        # => k<=i, 1<=j
        """
        有了 ❗️❗️❗️哨兵——左右大护法❗️❗️❗️ 之后，为啥不用初始化了？
        原因如下：
            其实本质，需要理解 i<1，j<1的区域
            d[i][j]表示sub_sums[:i]的范围内背包容量为j的最大值
            d[0][:]必然全部为0，d[:][0]同样为0
            因此结论：✅这个区域被左右护法guard住了
        """
        # transition
        for i in range(1, N+1):
            for j in range(1, Q+1):# j=0的时候，默认都是0
                d[i][j] = d[i-1][j] # 不选i
                if 0<=i-k: # 选择i，然后从前i-k范围内选择剩下的j-1个数
                    dist = d[i-k][j-1] + sub_sum[i]
                    # if j == 1 and i==3:print(i, sub_sum[i], dist,d[i][j] )
                    if d[i][j] < dist: # 找到更大值下标
                        d[i][j] = dist
                        record[i][j] = True    
                        
        # step 3: 记录下背包中到底放了哪些
        # 从 d[N-1][Q] 开始挨个逆向检索
        ans = []
        i, j = N, Q
        while 0<=i and 0<j:
            if record[i][j]:
                ans.append(i-k) # i-1被选择了
                i = i-k 
                j = j-1 # 继续查找背包容量为j-1的时候，哪些被选择了
            else: # i没有被选择，背包容量不变，继续向前搜索
                i = i-1
        print(sub_sum, record)
        return ans[::-1]

    # method 1: 01背包问题
    # 两步走：1）找到最大值；2）记录最大值对应序列下标
    # ❗️❗️❗️思路很重要：不能想当然，得逻辑自洽啊！！！
    def maxSumOfThreeSubarrays_1(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        # step 1: 先求解nums中以nums[i]结尾的子序列长度为k的序列和
        # preprocess
        # pre_sum[i]表示nums[:i]的和
        # 0<=i<=N
        pre_sum = list(accumulate(nums, initial=0))
        
        sub_sum = [0]*N
        for i in range(N):
            # 第一个k个元素子序列[0, k)
            if 0 <= i-k+1:
                sub_sum[i] = pre_sum[i+1] - pre_sum[i-k+1]
        
        # step 2: 开始条件背包
        # state: d[i][j]表示在sub_sum上前[0,i]范围内选取j个元素的最大值，且要求j个元素之间间隔为k
        # 0<=i<N; 0<=j<=3
        Q = 3
        d = [[0]*(Q+1) for i in range(N)]
        record = [[False]*(Q+1) for i in range(N)] # 用来记录背包容量为j的时候，i有没有被选择

        # initialization
        # 0<=i<N, 1<=i, k<=i; 0<=j<=3,1<=j
        # => k<=i, 1<=j
        
        # j==0
        for i in range(N):
            d[i][0] = 0
        # i<k；❗️❗️❗️这里的初始化极其不好想，最快的方法就是直接全部写出来
        for j in range(1, Q+1):
            d[k-1][j] = sub_sum[k-1]
            record[k-1][j] = True

        # transition
        for i in range(k, N):
            for j in range(1, Q+1):# j=0的时候，默认都是0
                # # 特殊处理 initialization，主要范围 k<=i, 1<=j 这部分的补集
                # if i<k: 
                #     # 由于i<k, 所以最多形成一个符合长度为k的区间，因此不管j为多少，以k-1为结尾的这个区间一定会被选择，放到背包中，才能形成最大值
                #     if i==k-1: # 正好形成一个，因此不管j为多少，以k-1为结尾的这个区间一定会被选择，放到背包中，才能形成最大值
                #         d[i][j] = sub_sum[k-1]
                #         record[k-1][j] = True
                #     else:
                #         # 无法形成以k-1为结尾的区间，全部默认为0
                #         ...
                #     continue  

                d[i][j] = d[i-1][j] # 不选i
                if 0<=i-k: # 选择i，然后从前i-k范围内选择剩下的j-1个数
                    dist = d[i-k][j-1] + sub_sum[i]
                    # if j == 1 and i==3:print(i, sub_sum[i], dist,d[i][j] )
                    if d[i][j] < dist: # 找到更大值下标
                        d[i][j] = dist
                        record[i][j] = True    
                        
        # step 3: 记录下背包中到底放了哪些
        # 从 d[N-1][Q] 开始挨个逆向检索
        ans = []
        i, j = N-1, Q
        while 0<=i and 0<j:
            if record[i][j]:
                ans.append(i-k+1) # i被选择了
                i = i-k 
                j = j-1 # 继续查找背包容量为j-1的时候，哪些被选择了
            else: # i没有被选择，背包容量不变，继续向前搜索
                i = i-1
        # print(sub_sum, record)
        return ans[::-1]