'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
# conbinatons of one element, two element, three...
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def dfs(nums,path,level):
            nonlocal ans
            if level==0:
                ans.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:],path[:]+[nums[i]],level-1)
                
        for i in range(1,len(nums)+1):
            dfs(nums,[],i)
        return ans