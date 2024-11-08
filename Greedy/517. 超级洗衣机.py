"""
[hard]

假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。

 

示例 1：

输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2   
示例 2：

输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     
示例 3：

输入：machines = [0,2,0]
输出：-1
解释：
不可能让所有三个洗衣机同时剩下相同数量的衣物。
 

提示：

n == machines.length
1 <= n <= 104
0 <= machines[i] <= 105

https://leetcode.cn/problems/super-washing-machines/description/?source=vscode
"""

"""
最佳答案：

https://leetcode.cn/problems/super-washing-machines/solutions/1023293/gong-shui-san-xie-noxiang-xin-ke-xue-xi-mzqia/?source=vscode
"""

# 题目意思理解，上来就理解错了：注意❗️任意选择 m 台机器，然后将这m台机器里面的衣服送到相邻机器里面，所以 [2, 0, 1, 0, 2] 最小移动步数为1，因为可以同时选择两台含有两件衣服的机器 {2, 2}，然后同时将里面的一件衣服送到相邻的一台洗衣机，就变成了 [1, 1, 1, 1, 1]，平衡了


class Solution:

    def findMinMoves(self, machines: List[int]) -> int:
        sumNum, lens = sum(machines), len(machines)
        # 判断是否每个洗衣机都能相同
        if sumNum % lens != 0: return -1
        avg, ans, pre = sumNum // lens, 0, 0
        for i in range(lens):
            # 前面洗衣机里已经有多少个衣服了
            pre += machines[i]
            # 前面的洗衣机还需要多少个衣服
            preNeed = pre - avg * (i + 1)
            # 举例子：
            # 0 0 11 5
            # MAX (最大值) 为               :11
            # avg (每个洗衣机需要的衣服) 为    :16 / 4 = 4
            #
            # 首先 MAX 最大为11 那么最少需要 11 - 4 = 7 次转移
            # 这就是 machines - avg 的意思
            #
            # 接下来是 preNeed
            # 比如第一个数 0 变成 4 那需要 (0,11,5) 向前转移4次
            # 比如第二个数 0 变为 4 就需要 (11,5) 向前转移8次 为什么! 因为前面的0 还需要4次!
            # (0,1) -> (1,1) -> (2,1) -> (3,1) -> (4,1) -> (4,2) -> (4,3) -> (4,4)
            # 所以前缀和 pre - avg * (i + 1) 就是前面需要转移的个数
            # 负数为缺少(需要后面往前转) 正数为多(需要向后转)
            # 当到第三个数的时候 preNeed等于 11 - 3 * 4 = -1 或有 (0,0,11) 需要 5 向前转移一次
            #
            # 最后就是比较:
            # 记录最大转移几次
            # 开始到当前位置需要转移几次
            # 当前位置需要转移几次
            # 取最大值，为何呢，因为可以同时转移
            # 只要转移的次数小于最大的转移几次就可以联动转移，所以只用取最大的
            ans = max(ans, abs(preNeed), machines[i] - avg)
        return ans