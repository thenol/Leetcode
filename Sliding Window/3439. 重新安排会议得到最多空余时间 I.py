"""
[medium] 
给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。

同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为 [startTime[i], endTime[i]] 。

你可以重新安排 至多 k 个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长 连续空余时间。

移动前后所有会议之间的 相对 顺序需要保持不变，而且会议时间也需要保持互不重叠。

请你返回重新安排会议以后，可以得到的 最大 空余时间。

注意，会议 不能 安排到整个活动的时间以外。

 

示例 1：

输入：eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

输出：2

解释：



将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。

示例 2：

输入：eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

输出：6

解释：



将 [2, 4] 的会议安排到 [1, 3] ，得到空余时间 [3, 9] 。

示例 3：

输入：eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

输出：0

解释：

活动中的所有时间都被会议安排满了。

 

提示：

1 <= eventTime <= 109
n == startTime.length == endTime.length
2 <= n <= 105
1 <= k <= n
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。

https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/?slug=find-valid-pair-of-adjacent-digits-in-string&region=local_v2
"""

"""
核心思路：
    【推理过程】
        <= 解一定覆盖所有可能性
        <= 贪心 or 动态规划
        <= 从提示知道，必然存在时间复杂度为 O(n) 或者 O(logn) 的解法
        
    【条件转化】
        <= 关键词：间的 相对 顺序需要保持不变
        <= 我们可以预处理出空闲的段，然后对于移动会议，其实就是将相邻的空闲段连接到一起，也就是合并一次就可以多选一个相邻的空闲段，如果有k次合并，那么就是最多可以选k+1个相邻空闲段。那么问题就变为维护一个窗口大小最大为k+1的窗口，滑动窗口解决即可。
    【归纳总结】
        <= 反向思考（移动会议变为合并空闲时间窗口） + 固定尺寸的滑动窗口
        <= 秘诀：最多k => 窗口大小为k+1
"""