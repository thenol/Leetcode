"""
[hard]

给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。

 
示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
 

提示：

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5

https://leetcode.cn/problems/russian-doll-envelopes/description/?source=vscode
"""

# 思路：
"""
【状态表示】
    d[i] 表示 表示以 i 结尾的最多能有多少个数； 0<=i<N
【转移方程】
    LIS模板题(O^2)
【初始化】
    ...
【数据规模】
    (10^5)^2 = 10^10 显然O(N^2)会TLE
    O(NlogN) = O(10^5*5) 显然OK 
    
"""

from math import inf
import bisect
class Solution:
    # method 2: 求LIS的长度——模板题
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        s_e = sorted(envelopes, key=lambda x: (x[0], -x[1])) # 这样排序，不至于让相同w的能够互相装入
        heights = [item[1] for item in s_e]
        # d[i]表示heights以i结尾的LIS

        ans = 0
        seq_tails = [inf]*len(s_e)
        seq_tails[0] = heights[0]
        for i in range(len(s_e)):
            idx = bisect.bisect_left(seq_tails, heights[i]) # 找到seq_tails不小于heights[i]最小下标值，说明放到这里，可以和之前的seq_tails形成尾部更小的递增序列
            seq_tails[idx] = min(seq_tails[idx], heights[i]) # 更新该序列的尾部值
            ans = max(ans, idx+1) # 统计当前 i 对应的 递增序列长度
        return ans
    
    # method 1: 
    def maxEnvelopes_1(self, envelopes: List[List[int]]) -> int:
        N = len(envelopes)

        # sorted
        sorted_envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        # filter height
        h_arr = [item[1] for item in sorted_envelopes]

        # state: d[i] 表示以 i 结尾的最多能有多少个数
        # 0<=i<N
        d = [0] * N

        # initializaiton
        seq_tails = [inf] * N
        seq_tails[0] = h_arr[0]
        d[0] = 1

        # transition
        # 边界如何处理，第一个元素单独处理成边界，从第二个开始
        for i in range(1, N):
            # ❌易错点：下标和序列长度换算
            seq_len = bisect.bisect_left(seq_tails, h_arr[i]) - 1
            seq_tails[seq_len + 1] = min(seq_tails[seq_len + 1], h_arr[i])
            d[i] = seq_len + 2
        
        return max(d)

