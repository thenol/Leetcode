"""
[medium]

你将会获得一系列视频片段，这些片段来自于一项持续时长为 time 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

使用数组 clips 描述所有的视频片段，其中 clips[i] = [starti, endi] 表示：某个视频片段开始于 starti 并于 endi 结束。

甚至可以对这些片段自由地再剪辑：

例如，片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, time]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

 

示例 1：

输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
输出：3
解释：
选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在手上的片段为 [0,2] + [2,8] + [8,10]，而这些覆盖了整场比赛 [0, 10]。
示例 2：

输入：clips = [[0,1],[1,2]], time = 5
输出：-1
解释：
无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
示例 3：

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
输出：3
解释： 
选取片段 [0,4], [4,7] 和 [6,9] 。
 

提示：

1 <= clips.length <= 100
0 <= starti <= endi <= 100
1 <= time <= 100

https://leetcode.cn/problems/video-stitching/description/?source=vscode
"""

import bisect
from math import inf
from operator import le
class Solution:
    # method 2: 固定排序右，逐个比较左
    # 聚焦到对元素本身的判断而非对下标的判断
    # 相比于方法1好在哪，先判断再处理，确保了边界的正确性，所见即所得
    # 但是方法1，先处理再判断，边界情况很复杂，
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        s_c = sorted(clips, key=lambda x: x[1])
        left = time
        cnt = 0
        left_most = inf
        # print(s_c)
        while s_c:
            if s_c[-1][1] < left: # 从后往前，如果最后的都没有time大，直接失败
                return -1
            while s_c and left <= s_c[-1][1]: # 找到所有满足有边界覆盖条件里面的，最左边界
                left_most = min(left_most, s_c.pop()[0])
            cnt += 1 
            left = left_most
            if not left: break # 如果提前到达0，直接退出，剪枝
        if left != 0: return -1 # 判断左边界是否到达
        return cnt

    # method 1: greedy
    # 错误原因，算法只是在贪心地寻找，右边界尽可能靠左的情况，而漏掉了，即使右边界靠右，但是左边界靠左的情况
    # 修正：左顾右盼
    # ❌： 退出状态很难判断——需要处理各种case
    def videoStitching_1(self, clips: List[List[int]], time: int) -> int:
        # state: 
        s_c = sorted(clips, key=lambda x: x[1])
        if s_c[-1][1] < time: return -1
        N = len(s_c)
        cnt = 0
        left = time # 初始认为是 [time, +inf]
        next_left = inf

        for i in range(N-1, -1, -1): # 逆序遍历s_c
            if left <= s_c[i][1] and s_c[i][0]:
                next_left = min(next_left, s_c[i][0]) # 寻找最左边界
            elif s_c[i][0] == 0:
                # 已经到起点
                cnt += 1
                break
            else: # s_c[i][1] < left
                cnt += 1 # 找到新的切分段
                left = next_left
        
        if i==0 and s_c[i][0]==0 and s_c[i][1] < left: 
            cnt +=1 
            
        return cnt 
        