'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# graph: dfs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums,path,level):
            nonlocal ans
            if level==0:
                ans.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:],path[:]+[nums[i]],level-1)
        
        ans=[]
        dfs([i for i in range(1,n+1)],[],k)
        return ans