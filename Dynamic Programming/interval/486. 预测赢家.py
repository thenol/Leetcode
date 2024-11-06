"""
[medium]

给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。

玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。

如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。你可以假设每个玩家的玩法都会使他的分数最大化。

 

示例 1：

输入：nums = [1,5,2]
输出：false
解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。 
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 false 。
示例 2：

输入：nums = [1,5,233,7]
输出：true
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。
 

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 107

https://leetcode.cn/problems/predict-the-winner/description/?source=vscode
"""

# 核心思路：区间dp
"""
【状态选择】

【转移方程】

【初始化】

【计算顺序】
"""

from itertools import accumulate
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        if N==1:return True
        # preprocess
        # sm[i]表示nums[:i]的前缀和
        sm = list(accumulate(nums, initial=0))

        # state: d[i][j] 表示在nums[i:j]上玩家先手取得的最大数
        # 0<=i<j<=len(nums)
        d = [[0]* (N+1) for i in range(N)]

        # initialization
        for i in range(N):
            d[i][i+1] = nums[i]
        # print(d)

        # transition
        # 0<=i<j<=len(nums)
        # i<=j-1
        # 错误计算顺序❌：计算方式为从上到下，从左到右，但是由于转移方程依赖左一和下一，所以此种方式时错误的方式
        # for i in range(N-1): # i==N-1时，j==N，边界已经处理完
        #     for j in range(i+1, N+1):
        #         # 先手选择：选择自己能赢的最大数 ———— 这种决策依赖于之前的决策
        #         # 先手选择：选择对手能选择的最小数 ———— 这种决策只依赖于未来的决策
        #         d[i][j] = sm[j] - sm[i] - min(d[i+1][j], d[i][j-1]) # 细节：空数组d[i][i]在上面初始化的时候已经被默认赋值为0了

        # 正确计算顺序✅：因为转移方程依赖左一和下一，所以计算方式为对角线型
        # ❗️最快换算方式：特殊值往里带最快啊
        for k in range(N-1): # 每次计算结束少一行，共计算N-1次
            for i in range(N-1-k): # k=0时候i只需遍历N-1行
                # 计算
                j = i + k + 2 # 判断左边界：当i=0, k=0时, j=2；也就是直接从d[0][2]开始计算就行了；判断右边界：当k=N-2时，i=0,j=N可以计算到右边界，因此成立；❗️注意：必须初始化
                d[i][j] = sm[j] - sm[i] - min(d[i+1][j], d[i][j-1]) # 细节：空数组d[i][i]在上面初始化的时候已经被默认赋值为0了

        # print(d)
        return d[0][N] >= sm[N]/2

    def predictTheWinner_1(self, nums: List[int]) -> bool:
        N = len(nums)
        if N==1:return True
        sm = list(accumulate(nums, initial=0))
        d = [[0]* (N+1) for i in range(N)]
        d[N-1][N] = nums[N-1] # 最后一行被填充

        for k in range(N-1): # 每次计算结束少一行，只需计算N-1次
            for i in range(N-1-k): # k=0时i可以遍历N行，但是转移方程中，d[i][j]依赖于下一和左一，因此只能让i遍历到第N-2行，此外最后一行需要初始化；最终k=0时，i遍历N-1行
                # 计算
                j = i + k + 1 # i=0, k=0, j=1
                d[i][j] = sm[j] - sm[i] - min(d[i+1][j], d[i][j-1]) # 细节：空数组d[i][i]在上面初始化的时候已经被默认赋值为0了
                # 0<=1+i<N, 0<=i<N-1
                # 0<=j-1<=N, 0<=j<=N
                
                # 当k取右边界时，
                #   当k=N-2时， i=0，此时 j=N-1
                #   当K=N-3时，i=[0,1]，此时j=[N-2, N-1]
                #   所以总是剩最后一列无法计算到

        print(d)
        return d[0][N] >= sm[N]/2
    