"""
[hard]

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

 

示例 1：



输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
示例 2：



输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。 
共获得报酬 150 = 20 + 70 + 60。
示例 3：



输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6
 

提示：

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4

"""

"""
最优解：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/

核心思路：
    * 【推理过程】
        <= 解的完备性知道一定遍历了所有情况
        <= 由提示知道，必然存在O(N)或者O(NlogN)解法
        <= 如果是O(N)解法，则动态规划子序列问题 或者 一次遍历
    * 【条件转化】
        <= 动态规划 -> 缩减问题，转化为子问题
    * 【归纳总结】
        二分 + 动态规划
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))  # 按照结束时间排序
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_left(jobs, (st + 1,), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
            # 状态转移中，为什么是 j 不是 j+1：上面算的是 > st，-1 后得到 <= st，但由于还要 +1，抵消了
            """
            理解：目标：查找 endTime[j] <= startTime[i] 的最大下标 j
            1. 但是 bisect_left 返回的是第一个大于等于 st 的下标，所以需要 -1
            实际过程：
                j = bisect_left(jobs, (st + 1,), hi=i) - 1 # 二分查找，找到第一个大于等于 st + 1 的下标（最低秩），然后 -1，得到最后一个小于等于 st 的下标（最高秩）
                f[i+1] = max(f[i], f[j+1] + p) # f[i] 表示区间 jobs[:i]的最大收益，f[j+1] 表示区间 jobs[:j+1]的最大收益，+ p 表示加上当前工作的收益

            """

            f[i + 1] = max(f[i], f[j] + p)
        return f[-1]
