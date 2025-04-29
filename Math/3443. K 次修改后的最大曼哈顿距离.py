"""
[medium]

给你一个由字符 'N'、'S'、'E' 和 'W' 组成的字符串 s，其中 s[i] 表示在无限网格中的移动操作：

'N'：向北移动 1 个单位。
'S'：向南移动 1 个单位。
'E'：向东移动 1 个单位。
'W'：向西移动 1 个单位。
初始时，你位于原点 (0, 0)。你 最多 可以修改 k 个字符为任意四个方向之一。

请找出在 按顺序 执行所有移动操作过程中的 任意时刻 ，所能达到的离原点的 最大曼哈顿距离 。

曼哈顿距离 定义为两个坐标点 (xi, yi) 和 (xj, yj) 的横向距离绝对值与纵向距离绝对值之和，即 |xi - xj| + |yi - yj|。

 

示例 1：

输入：s = "NWSE", k = 1

输出：3

解释：

将 s[2] 从 'S' 改为 'N' ，字符串 s 变为 "NWNE" 。

移动操作	位置 (x, y)	曼哈顿距离	最大值
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。

示例 2：

输入：s = "NSWWEW", k = 3

输出：6

解释：

将 s[1] 从 'S' 改为 'N' ，将 s[4] 从 'E' 改为 'W' 。字符串 s 变为 "NNWWWW" 。

执行移动操作过程中，距离原点的最大曼哈顿距离是 6 。

 

提示：

1 <= s.length <= 105
0 <= k <= s.length
s 仅由 'N'、'S'、'E' 和 'W' 。

https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/solutions/3061765/heng-zong-zuo-biao-fen-bie-ji-suan-tan-x-lhhi/?slug=maximum-manhattan-distance-after-k-changes&region=local_v2&tab=solutions&tab=3061765&tab=heng-zong-zuo-biao-fen-bie-ji-suan-tan-x-lhhi
"""
"""
    【推理过程】
        <= 解一定覆盖所有可能性
        <= 曼哈顿距离 -> 必然分开求解
        <= 由于需要覆盖所有可能性，必然 贪心 or 动态规划
    【条件转化】
        <= 找规律，思考修改一步的情况下，可以带来的增益，那么修改k次肯定能够带来最大增益
        <= 思考，对每一步修改k次之后，带来的增益是多少
    【归纳总结】
        找规律，冷静分析，思考每一步带来的增益
    
"""

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # 初始化答案为0，x和y坐标为0
        ans = x = y = 0
        
        # 遍历字符串中的每个字符及其索引
        for i, c in enumerate(s):
            # 根据字符更新坐标x和y
            if c == 'N': 
                y += 1  # 'N'表示向北移动，y坐标加1
            elif c == 'S': 
                y -= 1  # 'S'表示向南移动，y坐标减1
            elif c == 'E': 
                x += 1  # 'E'表示向东移动，x坐标加1
            else: 
                x -= 1  # 'W'表示向西移动，x坐标减1
            
            # 计算当前位置的曼哈顿距离，考虑最多进行k次操作来改变方向
            ans = max(ans, min(abs(x) + abs(y) + k * 2, i + 1))
            # max(当前最大距离, min(曼哈顿距离+k*2, 当前步数i+1))，这样可以限制最大步数
            # 比如刚开始走1步的时候，其实这个时候是没办法修改 k 次的，所以必须得取一个最小值
            # 当走的步数大于等于 k 的时候，才可以修改 k 次
        
        return ans  # 返回最大曼哈顿距离
