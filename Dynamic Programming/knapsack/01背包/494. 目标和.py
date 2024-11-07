"""
[medium]

给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
 

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

https://leetcode.cn/problems/target-sum/description/?source=vscode
"""

# 思路：01背包
# 易错点❌：没有找清楚背包的容量，误认为不管放正数还是负数，都是j，但是其实是错误的

"""
参考答案：见评论第一条

https://leetcode.cn/problems/target-sum/solutions/816361/mu-biao-he-by-leetcode-solution-o0cp/?source=vscode

"""


class Solution:
    # 正确✅：
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ...

    # 错误❌：Wrong Answer
    def findTargetSumWays_1(self, nums: List[int], target: int) -> int:
        # 01背包问题
        # state: d[i][j] 表示在前i范围数据中做选择为j的个数
        # 0<=i<len(nums)
        # 0<=j<=target
        N = len(nums)
        d = [[0]*(target+1) for i in range(N)]

        # initialization
        # for i in range(N):
        #     d[i][0] = 1
        for j in range(target+1):
            d[0][j] = 1 if j == nums[0] else 0
        
        d[0][0] = 0
        
        # transition
        # 1<=i
        for i in range(1, N):
            for j in range(target+1):
                # 不放i
                d[i][j] = d[i-1][j]

                # 能放下i；两种放法
                if 0<=j-nums[i] and 0<=d[i-1][j-nums[i]]:
                    d[i][j] += d[i-1][j-nums[i]]
                if j+nums[i] < target+1 and 0<=d[i-1][j+nums[i]]:
                    d[i][j] += d[i-1][j+nums[i]]
        print(d)
        return d[N-1][target]
        