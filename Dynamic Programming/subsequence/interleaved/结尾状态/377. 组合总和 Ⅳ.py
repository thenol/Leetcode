"""
[meidum]

给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000
 

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

https://leetcode.cn/problems/combination-sum-iv/description/?source=vscode
"""
# 核心思路： 
#  method 1: 最简单容易想到的就是dfs方法
#  method 2: 其次容易想到动态规划 d[target] 表示 target的组合数
"""
基于method 2: 状态转移方程如下，即d[i]只依赖于其前序序列，因此可以按照如下迭代式编写，另外本质上是子序列问题
for i in range(2, target+1):
    for num in nums:
        if num == i:
            d[i] += 1
        elif i-num > 0:
            d[i] += d[i-num]
"""

class Solution:
    # dp
    # 稳如老狗按部就班法
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # state: d[i]表示i的所有组合数量
        # 0<=i<=target
        N = len(nums)
        d = [0]*(target + 1)
        d[1] = 1 if 1 in nums else 0
        for i in range(2, target+1):
            for num in nums: # 对于每一个target或者i寻找所有的num组合
                if num == i: # 找到一种组合
                    d[i] += 1
                elif i-num > 0: # 递归深入继续寻找target-num组合
                    d[i] += d[i-num]

        return d[target]
    
    # 极致三刀流骚操作法
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # state: d[i]表示所有组合为i的数量
        # 0<=i<=target
        N = len(nums)
        d = [0] * (target+1)
        d[0] = 1 # 归约态：0不需要再找数，一定存在
        for i in range(target+1):
            for j in nums:
                if 0<=i-j:
                    d[i] += d[i-j]
        return d[target]


    # dfs + cache
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        # state: ..
        N = len(nums)
        @cache
        def dfs(target):
            """返回target所有组合数量"""
            nonlocal nums
            if target < 0:
                return 0
            if target == 0:
                return 1
            
            ans = 0
            for num in nums:
                ans += dfs(target-num)
            
            return ans
            
        return dfs(target)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # d[i][j]表示以nums[i]结尾的形成target为j的所有组合
        # 0<=i<N; 0<=j<=target
        N = len(nums)

        # method 1: 完全背包内容来理解
        # @cache
        # def f(i, j):
        #     nonlocal N, nums

        #     ans = []
        #     # 不选择 i
        #     if 0<=i-1:
        #         ans = f(i-1, j)
        #     # 选择i
        #     if 0 == j-nums[i]:
        #         ans.append([nums[i]])
        #     elif 0 < j-nums[i]:
        #         res = f(i, j-nums[i])
        #         for item in res:
        #             ans.append([nums[i]] + item)
        #     return ans
        # return f(N-1, target)
        """
        成功记录选择的内容
        [[1,1,1,1],[2,1,1],[2,2],[3,1]]
        """

        # method 2: 回溯
        @cache
        def dfs(i, j):
            nonlocal N, nums
            if j == 0: return 1

            ans = 0
            for k in range(i):
                if 0<=j-nums[k]:
                    ans += dfs(i, j-nums[k])
            return ans
        
        return dfs(N, target)