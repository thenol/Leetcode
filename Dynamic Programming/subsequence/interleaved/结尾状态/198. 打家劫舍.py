"""
[medium]

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

https://leetcode.cn/problems/house-robber/description/

"""

# 总结：
"""
非连续子数组类型，可以类比连续子数组类型题目
"""

# 思路：简单

class Solution:
    # method 2: 范围状态
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]

        # before和last分别表示到当前为止，前天和昨天的最大收益
        before, last = nums[0], max(nums[1], nums[0]) 

        for i in range(2, N):
            before, last = last, max(before + nums[i], last) # 当前抢：只能从前天before转移而来；不抢：只能从昨天last转移而来
        return last

    # method 1: 结尾状态——可以选择任意子序列
    def rob(self, nums: List[int]) -> int:
        # state: d[i] 表示以 i 为末尾元素，最高金额
        d = [item for item in nums]
        
        # initialization

        # transition
        for i in range(len(nums)):
            for j in range(i-1):
                d[i] = max(d[i], d[j]+nums[i])
        
        return max(d)
    
    # method 2: 结尾状态——限制选择，必须选择d[i-2]
    # ❌ 反例[2,1,1,2]，最大值为{2,2}
    def rob(self, nums: List[int]) -> int:
        # state: d[i]以i结尾的最高金额
        N = len(nums)
        d = [_ for _ in nums]
        for i in range(N):
            if 0<=i-2:
                d[i] = max(d[i], d[i-2]+nums[i])
        print(d)
        return max(d)
    
    # method 3: 范围状态——选择或者不选择末尾元素
    # ❌
    def rob(self, nums: List[int]) -> int:
        # state: d[i]表示到i的最大值
        N = len(nums)
        d = [_ for _ in nums]

        for i in range(N):
            d[i] = d[i-1] # 不选nums[i]
            # 选择nums[i]，就必须不能选择nums[i-1]，但是范围状态，或者当前最优解是整个集合的最优解，也就是d[0,...,i]的最优解，无法表达选择nums[i]，而不选择nums[i-1]的转移方程，即使有办法选择，也不知道当前 d[i] 到底选择了哪些元素。言下之意，无法看出结果中选择了哪些元素，从而返回去，再合法性得修改选择的元素。
            
            # 简而言之：当前的是结果，不可能看出来历史里面的细枝末节，更不可能再回去修改历史，来重新获得结果
            ...