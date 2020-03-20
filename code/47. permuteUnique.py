'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(nums,path):
            if not nums:
              res.append(path)
            else:
                last='' # use last to remember variable just selected
                for i in range(len(nums)):
                    if not nums[i]==last: # skip the variable just selected
                        dfs(nums[:i]+nums[i+1:],path+[nums[i]])
                        last=nums[i]

        dfs(sorted(nums),[]) # Deduplication, sorted()
        return res