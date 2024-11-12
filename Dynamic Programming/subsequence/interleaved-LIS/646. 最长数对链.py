"""
[medium]

给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。

现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。

找出并返回能够形成的 最长数对链的长度 。

你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

 

示例 1：

输入：pairs = [[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4] 。
示例 2：

输入：pairs = [[1,2],[7,8],[4,5]]
输出：3
解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。
 

提示：

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000

https://leetcode.cn/problems/maximum-length-of-pair-chain/description/?source=vscode
"""

# 核心思路：排序之后为连续递增子序列问题
# 最优时间复杂度 O(NlogN)

import bisect
from math import inf
class Solution:

    # 最长递增子序列问题——子序列顺序可变

    # method 1: O(N^2)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # preprocess
        pairs = sorted(pairs)

        # state: d[i] 表示以i结尾的最长数对链长度
        # 0<=i<N
        N = len(pairs)
        d = [1]*N

        # initialization
        ...

        # transition
        for i in range(N):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    d[i] = max(d[i], d[j]+1)
        
        return max(d)
    
    # method 2: O(NlogN)——dp + 二分
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # preprocess
        pairs = sorted(pairs) # 可以调换顺序

        # state: d[i] 表示以i结尾的最长数对链长度
        # 0<=i<N
        N = len(pairs)
        d = [1]*N
        t = [inf]*N # t[i] 表示所有序列长度为i+1的最小末尾值

        # initialization
        ...

        # transition
        for i in range(N):
            idx = bisect.bisect_left(t, pairs[i][0]) # 找到不小于当前值的最小秩，用于存放当前值
            t[idx] = min(t[idx], pairs[i][1]) # 注意lefti < righti，所以正确性依然成立，整体链中，所有数都是严格递增的
            d[i] = idx + 1 # 最长序列长度
        """
        input: [[1,2],[4,5],[7,8]]
        举例说明
        d: [1, 2, 1] 
        t: [2, 5, inf]
        当前 i = 2: pairs[2] = [7, 8]
        step 1. 
            二分查找： bisect.bisect_left(t, 7)，找出idx = 2，也就是不小于7（4<=）的最小秩。说明：当前7可以放到t中的5后面，从而形成序列长度为3的严格递增序列，
        step 2. 
            更新t：t[idx=2] = min(5, 8) = 8, 将序列长度为idx+1=3的递增序列最小的末尾值更新为8
        step 3. 
            更新d[i=2]的长度为 idx+1 = 3
        
        最终：
        d: [1, 2, 3] 
        t: [2, 5, 8]
        """
        print(d, t)
        return max(d)