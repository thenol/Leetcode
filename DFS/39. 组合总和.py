"""
[medium]

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40

https://leetcode.cn/problems/combination-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
能排序排序
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(nums, target, path, start):
            if target == 0:
                ans.append(path)
            for i in range(start, len(nums)):
                if target - nums[i] >= 0:
                    dfs(nums, target-nums[i], path + [nums[i]], start=i)
                else:
                    break
        candidates.sort()
        dfs(candidates, target, [], start=0)
        return ans
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #recursive
        res=[]
        for k,v in enumerate(candidates):
            if target-v==0:
                # print(i)
                res.append([v])
            elif target-v>0:
                r=self.combinationSum(candidates[k:],target-v)
                for i in r:
                    res.append([v]+i)
            
        return res