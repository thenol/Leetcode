"""
[hard]

一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 1 个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

 

示例 1：

输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
示例 2：

输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
 

提示：

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones 按严格升序排列

https://leetcode.cn/problems/frog-jump/description/?source=vscode
"""

# 核心思路：间断子序列问题 + 条件状态转移
"""
【状态表示】 
    1. d[i]表示以i结尾的是否可以跳跃
    2. 0<=i<len(stones)
【状态转移】
    ...
【初始化】
    1. 初始化0
"""

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # state: d[i]表示以i结尾的是否可以跳跃
        # 0<=i<len(stones)
        N = len(stones)
        d = [False] * N
        cond = [set() for i in range(N)] # 表示i跳跃成功的步数集合
        
        # initialization
        d[0] = True
        cond[0].add(1)

        # transition
        for i in range(1, N): # 特殊值单独处理，从1开始问题更加简单
            for j in range(i): 
                if (stones[i] - stones[j]) in cond[j] and d[j]:
                    d[i] = d[i] or d[j]
                    k = (stones[i] - stones[j])
                    cond[i] |= {k-1, k, k+1}
                    # break # 贪心：步数越长，后面可以活动的范围越大；
                    # 贪心是错误❌：因为最长的步伐也可能导致无法到达，注意步伐是离散值，只有在{k-1,k,k+1}中的时候，才会到达
                    # 此处还有一个技巧，没有改遍历[k-1, k, k+1]为哈希集合，可以加速判断，空间换时间；否则可能会TLE
        
        # print(d)
        # print(cond)
        return d[N-1]
       