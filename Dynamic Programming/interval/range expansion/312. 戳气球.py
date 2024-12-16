"""
[hard]

有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

 

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
示例 2：

输入：nums = [1,5]
输出：10
 

提示：

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100

https://leetcode.cn/problems/burst-balloons/description/?source=vscode
"""

# 核心思路：
"""
1. 方式1: 先打爆
第一种方式正着打爆，即先打爆，状态为 f(i, j)这种情况下，f(i, j)有后效性，无法形成有效的子问题，无法做决策，依赖外部可变情况，无法有效拆分可能性，例如：
 1, a, b, c, d, e, 1
 0, 1, 2, 3, 4, 5, 6
顺序1：第一次打爆：d，则剩下：(a, b, c) (e)，此时再打爆 c，则剩下 (a, b) (e)，这个时候，再打爆b的时候，右侧气球是 e
顺序2：第一次打爆：c，则剩下：(a, b) (d e)，                               这个时候，再打爆b的时候，右侧气球是 d

明显 针对 f(1,3) 决策或者拆分可能性的时候，右侧条件变化，无法进行，本质原因是 条件变量 (i, j) 表达能力不够

2. 方式2: 后打爆
第二种方式反着打爆，即后打爆，状态同样为 f(i, j)，但是此时后效性消除，可以有效表达题目含义，和决策，例如：
 1, a, b, c, d, e, 1
 0, 1, 2, 3, 4, 5, 6
顺序：想要打爆c，但是 c 最为最后打爆，这个时候，需要先打爆，f(1, 3)，即把(a, b)打爆完，把f(4, 6)打爆，即把(d, e)打爆完，这个时候，最后打爆 c 的时候，可以清楚地发现 c 的左侧和右侧 分别是 [0], [6]，也就是说最后打爆 c 的时候，左右边界都可知，此时可以清晰决策

"""

# 核心思路：由变转定；
"""
先打爆无法决策，同时也不是最优，后打爆一切就都确定了
"""

from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # state: d[i][j]为最后打爆nums[i:j]的获得硬币的最大数量
        # 0<=i<N; 0<=j<=N
        arr = [1] + nums + [1]
        N = len(arr)
        @cache
        def f(i, j):
            """打爆nums[i:j]的获得硬币的最大数量"""
            nonlocal arr, N
            # initialization
            if i==j: return 0 # 没有气球，非法情况，全部默认值0
            if i==j-1: return arr[i-1]*arr[i]*arr[j] # ⭕️只有一个气球，不是只返回当前气球，注意 i 左右两侧还有其他气球啊 ❗️

            # transition
            ans = 0
            ans = max( 
                ans, 
                f(i+1, j) + arr[i-1]*arr[i]*arr[j], # 最后打掉i
                f(i, j-1) + arr[i-1]*arr[j-1]*arr[j] # 最后打掉j-1
            )
            for k in range(i+1, j-1):
                ans = max(
                    ans, 
                    f(i,k) + f(k+1, j) + arr[i-1]*arr[k]*arr[j]) # 最后打掉k
            return ans
        return f(1, len(nums)+1)