"""
[meidum]

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
 

提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100

https://leetcode.cn/problems/ones-and-zeroes/description/?source=vscode
"""

# 核心思路：0/1背包问题
# 只不过放包里的是放两件物品

from collections import Counter
from functools import cache
class Solution:
    # 哨兵护法写法
    # 最推荐写法，比较有意义——归约态从范围变成了单点
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # preprocess
        strs_cnt = []
        for str in strs:
            cnt = Counter(str)
            strs_cnt.append((cnt['0'],cnt['1']))
        
        # 0/1 knapsack problem
        # state: d[i][m][n] 表示前i个元素，剩余容量为m和n的最大子集长度
        # 0<=i<len(strs)

        # initialization
        ...

        # transition
        @cache
        def f(i, m, n):
            """表示范围strs_cnt[:i]，剩余容量为m和n的最大子集长度"""
            nonlocal strs_cnt
            if i == 0: return 0 # 空数组，没元素可选了，返回0
            zero_cnt, one_cnt = strs_cnt[i-1]
            if 0 <= m-zero_cnt and 0<=n-one_cnt:
                # 放得下，可放可不放
                return max(f(i-1, m-zero_cnt, n-one_cnt) + 1, f(i-1, m, n))
            else: # 放不下
                return f(i-1, m, n)
        return f(len(strs), m, n)

    # 
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # preprocess
        strs_cnt = []
        for str in strs:
            cnt = Counter(str)
            strs_cnt.append((cnt['0'],cnt['1']))
        
        # 0/1 knapsack problem
        # state: d[i][m][n] 表示前i个元素，剩余容量为m和n的最大子集长度
        # 0<=i<len(strs)

        # initialization
        ...

        # transition
        @cache
        def f(i, m, n):
            """表示前i个元素，剩余容量为m和n的最大子集长度"""
            nonlocal strs_cnt
            if i < 0: # 没元素可选了，返回0
                return 0 
            zero_cnt, one_cnt = strs_cnt[i]
            if 0 <= m-zero_cnt and 0<=n-one_cnt:
                # 放得下，可放可不放
                return max(f(i-1, m-zero_cnt, n-one_cnt) + 1, f(i-1, m, n))
            else: # 放不下
                return f(i-1, m, n)
        return f(len(strs)-1, m, n)
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zero_one_list = []
        for s in strs:
            cnt = Counter(s)
            zero_one_list.append((cnt['0'], cnt['1']))
        
        N = len(zero_one_list)

        @cache
        def f(i, j, k):
            """到strs[i]，最多j个0，k个1"""
            nonlocal zero_one_list

            # 归约态
            if i==0:
                if zero_one_list[0][0]<=j and zero_one_list[0][1]<=k: return 1
                else: return 0

            ans = 0
            # 不装i
            if 0 <= i-1:
                ans = max(ans, f(i-1, j, k))
            
            zero, one = zero_one_list[i]
            # 可以装i
            if zero<=j and one <=k and 0<=i-1:
                ans = max(ans, f(i-1, j-zero, k-one) + 1)
            return ans
        return f(N-1, m, n)
