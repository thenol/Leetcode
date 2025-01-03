"""
[medium]

你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:

difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。

举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。

 

示例 1：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100 
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
示例 2:

输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0
 

提示:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105

https://leetcode.cn/problems/most-profit-assigning-work/description/?source=vscode
"""

# 核心思路：看数据规模，如果O(N^2)将超时

from collections import Counter
import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # preprocess
        # 工人统计，降低时间复杂度
        worker_group = Counter(worker)
        # 工作强度强度排序
        dp_bind = list(zip(difficulty, profit))
        dp_bind = sorted(dp_bind, key=lambda x: x[0])
        # d[i]表示以工作难度不大于difficulty[i]能获取到的最大收益，加速查找，降低时间复杂度
        N = len(difficulty)
        d = [0]*N
        d[0] = dp_bind[0][1]
        for i in range(1, N):
            d[i] = max(dp_bind[i][1], d[i-1])
        
        ans = 0
        dp_bind_d = [item[0] for item in dp_bind]
        for k, v in worker_group.items():
            # 二分查找，降低时间复杂度
            idx = bisect.bisect_right(dp_bind_d, k)
            if idx - 1 < 0:
                continue
            else:
                ans += (d[idx-1])*v
        
        return ans
        

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        z = zip(difficulty, profit)
        zs = sorted(z, key=lambda x:x[0])
        zs.append((inf, 0)) # 加上哨兵
        worker.sort()
        
        i, j = 0, 0
        maxP = 0
        ans = 0
        while i<len(worker) and j<len(zs):
            d, p = zs[j]
            if worker[i] < d:
                ans += maxP
                i += 1
                continue
            else:
                maxP = max(p, maxP)
                j += 1
        return ans