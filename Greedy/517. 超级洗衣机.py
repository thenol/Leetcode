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

https://leetcode.cn/problems/super-washing-machines/solutions/1023234/acmjin-pai-ti-jie-tan-xin-bian-cheng-xio-mp7n/?source=vscode
"""

# 题目意思理解，上来就理解错了：注意❗️任意选择 m 台机器，然后将这m台机器里面的衣服送到相邻机器里面，所以 [2, 0, 1, 0, 2] 最小移动步数为1，因为可以同时选择两台含有两件衣服的机器 {2, 2}，然后同时将里面的一件衣服送到相邻的一台洗衣机，就变成了 [1, 1, 1, 1, 1]，平衡了


class Solution:
    def findMinMoves(self, machines):
        ans = 0
        total_sum = sum(machines)
        presum = 0
        n = len(machines)
        
        # If total sum is not divisible by the number of machines, return -1
        if total_sum % n != 0:
            return -1
        
        avg = total_sum // n
        
        for i in range(n):
            presum += machines[i]
            ans = max(
                ans, 
                max(
                    machines[i] - avg, # 统计衣服最多的那个洗衣机至少需要转移的次数
                    abs(presum - avg * (i + 1)) # 统计对每个洗衣机来说，至少要经过的衣服的数量，即经过 i 让 i 的左右两侧均衡
                )
            )
        
        return ans
