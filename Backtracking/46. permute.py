
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursive
        # space complexity O(1)
        if len(nums)==1:
            return [nums]
        res=[]
        for i in range(len(nums)): # include itself
            nums[i],nums[len(nums)-1]=nums[len(nums)-1],nums[i]
            for v in self.permute(nums[0:len(nums)-1]):
                res.append(v+[nums[len(nums)-1]])
            nums[i],nums[len(nums)-1]=nums[len(nums)-1],nums[i]
        return res



        #backtrack of dfs
        # space complexity O(nlogn)
        '''
        class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            # backtrack or dfs
            def backtrack(nums,track):
                if not nums:
                    res.append(track[:])
                    return
                else:
                    for k,v in enumerate(nums):
                        track.append(v)
                        backtrack(nums[:k]+nums[k+1:],track)
                        track.pop()
            res=[]
            backtrack(nums,[])
            return res


        '''

        # dfs 
        '''
        class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:

            res = []
            def dfs(nums, path):
                if not nums:
                    res.append(path[:])
                    return
                for i in range(len(nums)):
                    dfs(nums[:i]+nums[i+1:], path + [nums[i]])

            res = []
            dfs(nums, [])
            return res
        '''

