"""
[meidum]

给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

https://leetcode.cn/problems/partition-equal-subset-sum/description/?source=vscode
"""

from itertools import accumulate
# 背包问题解决了从一群数中，选择任意子序列求和的问题
class Solution:
    # 背包问题；同时也可以意识到d[i],d[l][r]无法给出合理转移方程
    # 次题卡在：状态转移没搞懂
    def canPartition(self, nums: List[int]) -> bool:
        # state: d[i][j] 表示前i个元素是否可以分割出和为j的子集
        # 0<=i<N; 0<=j<=sum(nums)
        N = len(nums)
        s = sum(nums)
        if s % 2 != 0:return False
        half = s//2
        d = [[False] * (half+1) for i in range(N)]

        # initializaiton
        # 0<=j-item
        # j==0: True
        for i in range(N):
            d[i][0] = True # j已经成功装完了，自然为True
        # i==0: False
        
        # transition
        for i in range(1,N): # 在[0,i)上判断
            for j in range(half+1): # 当背包容量为j时
                d[i][j]=d[i-1][j] # 易错点❌：转移方程遗漏：这里先假设i放不下，因此前i个元素，能否装入j，就由前i-1个决定了
                if 0<=j-nums[i]: # 关注i是否放入背包，放得下
                    d[i][j] = d[i][j] or d[i-1][j-nums[i]] # 当前选择了i，判断[0, i)之前能不能成立
                # 错啦：放不下，不处理
                # 即使第i个放不下，d[i][j]也不一定是False啊，得看d[i-1][j]的状态
        # print(d)

        # 为什么不用三重循环：因为再遍历k的话，会重复计算，前面都已经算完了，对于i，只依赖于左边和上面，没有必要再遍历k再算一次
        return d[N-1][half]

    # TLE 版本——回溯
    def canPartition_2(self, nums: List[int]) -> bool:
        # state: 
        s = sum(nums)
        if s % 2 == 1: return False
        def dfs(nums, sm):
            """sm - item范围为R"""
            if sm == 0:
                return True
            if sm < 0:
                return False
            
            ans = False
            for i, item in enumerate(nums):
                ans = ans or dfs(nums[:i]+nums[i+1:], sm - item)
            
            return ans
        
        return dfs(nums, s//2)
            

    # WA版本：反例  [2,2,1,1]
    def canPartition_1(self, nums: List[int]) -> bool:
        # 先排序；
        N = len(nums)
        nums = sorted(nums)
        pre_sum = list(accumulate(nums, initial=0))
        # state: d[i]表示nums[:i]的和
        for i in range(N):
            if pre_sum[i] == pre_sum[N] - pre_sum[i]:
                return True
        return False    
  