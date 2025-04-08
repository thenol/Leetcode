"""
[medium]

给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。

同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为 [startTime[i], endTime[i]] 。

你可以重新安排 至多 一个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长 连续空余时间。

请你返回重新安排会议以后，可以得到的 最大 空余时间。

注意，会议 不能 安排到整个活动的时间以外，且会议之间需要保持互不重叠。

注意：重新安排会议以后，会议之间的顺序可以发生改变。

 

示例 1：

输入：eventTime = 5, startTime = [1,3], endTime = [2,5]

输出：2

解释：



将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。

示例 2：

输入：eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

输出：7

解释：



将 [0, 1] 的会议安排到 [8, 9] ，得到空余时间 [0, 7] 。

示例 3：

输入：eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

输出：6

解释：



将 [3, 4] 的会议安排到 [8, 9] ，得到空余时间 [1, 7] 。

示例 4：

输入：eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

输出：0

解释：

活动中的所有时间都被会议安排满了。

 

提示：

1 <= eventTime <= 109
n == startTime.length == endTime.length
2 <= n <= 105
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。

https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/description/?slug=reschedule-meetings-for-maximum-free-time-ii&region=local_v2
"""

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        计算在给定事件时间范围内可以安排的最大空闲时间
        
        参数:
            eventTime: 总事件时间长度
            startTime: 各个事件开始时间的列表
            endTime: 各个事件结束时间的列表
            
        返回:
            可以安排的最大空闲时间
        """
        
        # 计算所有空闲时间段:
        # 1. 第一个事件开始前的空闲时间
        # 2. 各事件之间的空闲时间
        # 3. 最后一个事件结束后的空闲时间
        free = [startTime[0]] + [s - e for s, e in zip(startTime[1:], endTime)] + [eventTime - endTime[-1]] # 空闲间隔数量比会议间隔数量多1

        # 初始化三个变量来存储最大的三个空闲时间段的索引
        a = b = c = -1  # a是最大的，b是第二大的，c是第三大的
        
        # 遍历所有空闲时间段，找出最大的三个
        for i, sz in enumerate(free):
            if a < 0 or sz > free[a]:
                a, b, c = i, a, b  # 发现更大的，依次向后移动
            elif b < 0 or sz > free[b]:
                b, c = i, b
            elif c < 0 or sz > free[c]:
                c = i

        ans = 0  # 初始化最大空闲时间
        
        # 遍历所有事件间隔，计算可能的最大空闲时间组合
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s  # 当前事件的持续时间
            
            # 检查是否可以合并相邻的空闲时间段；如果和最大的a,b,c空闲时间段不重叠，则将会议转移至前面空闲时间段
            # 注意❗️：空闲间隔数量比会议间隔数量多1，或者认为 一个空闲时间段 对应于 一个会议时间段，最后末尾是一个空闲时间段
            #     关系判断：i == a 意味着 当前 空闲时间段在当前会议的前面
            #     关系判断：i + 1 == a 意味着 当前 空闲时间段在当前会议的后面
            #     关系判断：sz <= free[a] 意味着 当前会议的持续时间小于等于最大的空闲时间段
            #     关系判断：sz <= free[b] 意味着 当前会议的持续时间小于等于第二大的空闲时间段
            #     关系判断：sz <= free[c] 意味着 当前会议的持续时间小于等于第三大的空闲时间段
            # 条件判断逻辑:
            # 如果当前事件不是最大的三个空闲时间段之一，或者事件持续时间小于等于某个大空闲时间段
            # 则可以尝试合并空闲时间段
            if i != a and i + 1 != a and sz <= free[a] or \
               i != b and i + 1 != b and sz <= free[b] or \
               sz <= free[c]:
                # 可以合并三个连续的空闲时间段（前一个、当前事件时间、后一个）
                ans = max(ans, free[i] + sz + free[i + 1])
            else:
                # 否则只能合并两个连续的空闲时间段
                ans = max(ans, free[i] + free[i + 1])
                
        return ans