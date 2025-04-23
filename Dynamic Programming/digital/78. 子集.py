"""
[medium]
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

https://leetcode.cn/problems/subsets/description/
"""

class Solution:
    # method 1: bit manipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1<<n): # 1 << len(nums) 计算2的n次方（n是nums的长度），即所有子集的数量
            subset = [x for j, x in enumerate(nums) if i>>j & 1] # 和每个数进行比较，如果i的第j位为1，则将nums[j]加入子集
            ans.append(subset)
        return ans
    
    # method 2: backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def dfs(nums,path,level):  # level 即 length 个元素组合
            nonlocal ans
            if level==0:
                ans.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:],path[:]+[nums[i]],level-1) # 选择 i ，继续下次选择
                
        for i in range(1,len(nums)+1):
            dfs(nums,[],i)
        return ans