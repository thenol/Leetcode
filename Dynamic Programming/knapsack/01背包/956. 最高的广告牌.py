"""
[hard]

你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。

返回 广告牌的最大可能安装高度 。如果没法安装广告牌，请返回 0 。

 

示例 1：

输入：[1,2,3,6]
输出：6
解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
示例 2：

输入：[1,2,3,4,5,6]
输出：10
解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
示例 3：

输入：[1,2]
输出：0
解释：没法安装广告牌，所以返回 0。
 

提示：

0 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000

https://leetcode.cn/problems/tallest-billboard/description/?source=vscode
"""

from functools import cache
class Solution:
    # method 1: 状态压缩dp
    # 分析：问题转化为是否可以删掉若干个元素，使得剩下的分割成两个和相等的子集
    # 从0 <= rods.length <= 20 知道，应该用状态压缩dp
    # 结果：MLE
    def tallestBillboard(self, rods: List[int]) -> int:
        # state: d[mask][half] 表示选择了{mask}集合是否能构成half
        N = len(rods)
        S = sum(rods)
        half = S // 2

        @cache
        def f(i, j):
            """表示选择了j集合是否能构成j"""
            nonlocal N, rods

            # initialization
            if j==0: return [i]
            if j<0: return []

            # transition
            ans = []
            for k in range(N):
                if (i>>k)&1 : continue # 选过了，跳过
                digits = f(i^(1<<k), j-rods[k])
                ans.extend(digits)
            return ans

        ans = False
        for j in range(half, -1, -1):
            digits = f(0, j)
            for digit in digits:
                if 0<len(f(digit, j)): # 没选择的继续选择
                    return j
        return 0
