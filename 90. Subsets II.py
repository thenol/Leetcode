'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[[]]
        def dfs(nums,path,level):
            nonlocal ans
            if level==0:
                ans.append(path)
            else:
                last=''
                for i in range(len(nums)):
                    if not nums[i]==last:
                        dfs(nums[i+1:],path[:]+[nums[i]],level-1)
                        last=nums[i]

        for i in range(1,len(nums)+1):
            dfs(nums,[],i)
        return ans