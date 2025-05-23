"""
[hard]

电子游戏“辐射4”中，任务 “通向自由” 要求玩家到达名为 “Freedom Trail Ring” 的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 ring ，表示刻在外环上的编码；给定另一个字符串 key ，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring 的第一个字符与 12:00 方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

旋转 ring 拼出 key 字符 key[i] 的阶段中：

您可以将 ring 顺时针或逆时针旋转 一个位置 ，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
 

示例 1：



 
输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
示例 2:

输入: ring = "godding", key = "godding"
输出: 13
 

提示：

1 <= ring.length, key.length <= 100
ring 和 key 只包含小写英文字母
保证 字符串 key 一定可以由字符串  ring 旋转拼出
"""

# 核心思路：聚焦增量，寻找子问题
# 本质是子序列问题，但是元素之间的转移，不是线性转移，而是环形转移

from collections import defaultdict
from functools import cache
from math import inf
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        # preprocess
        left = [defaultdict(lambda: inf) for _ in range(N)]
        right = [defaultdict(lambda: inf) for _ in range(N)]

        for i in range(N):
            j = (i + 1) % N # 向右走一圈
            right[i][ring[i]] = 0
            while j!=i:
                right[i][ring[j]] = min(right[i][ring[j]], (j-i+N)%N) # 计算j在i右侧举例的时候：(j-i+N)%N
                j = (j+1) % N
        
        for i in range(N):
            j = (i-1+N)%N
            left[i][ring[i]] = 0
            while j!=i:
                left[i][ring[j]] = min(left[i][ring[j]], (i-j+N)%N) # 计算 j在i左侧的时候：(i-j+N)%N；例如，即使 [1,2,3,4,5]，j=4, i=2的时候，N=5， i向左走 (2-4+5)%5 = 3，即2向左走3步到4
                j = (j-1+N) % N

        M = len(key)
        # state: d[i][k] 表示当前在i匹配完key[k]的最小steps
        # 0<=k<=M
        @cache
        def f(i, k):
            if k == M-1: 
                return min(left[i][key[k]], right[i][key[k]])

            ans = inf
            if k+1 <= M:
                ans = min(ans, 
                f((i+right[i][key[k]])%N, k+1) + right[i][key[k]], 
                f((i-left[i][key[k]]+N)%N, k+1) + left[i][key[k]]) # 向右、向左
            return ans
        
        return f(0, 0)+M
    
    # 哨兵写法
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        # preprocess
        left = [defaultdict(lambda: inf) for _ in range(N)]
        right = [defaultdict(lambda: inf) for _ in range(N)]

        for i in range(N):
            j = (i + 1) % N # 向右走一圈
            right[i][ring[i]] = 0
            while j!=i:
                right[i][ring[j]] = min(right[i][ring[j]], (j-i+N)%N)
                j = (j+1) % N
        
        for i in range(N):
            j = (i-1+N)%N
            left[i][ring[i]] = 0
            while j!=i:
                left[i][ring[j]] = min(left[i][ring[j]], (i-j+N)%N)
                j = (j-1+N) % N

        M = len(key)
        # state: d[i][k] 表示当前在i匹配完key[:k]的最小steps
        # 1<=k<=M;；如果k==0，则是空数组，没有字符
        @cache
        def f(i, k):
            if k == M: 
                return min(left[i][key[k-1]], right[i][key[k-1]])

            ans = inf
            if k+1 <= M:
                ans = min(ans, 
                f((i+right[i][key[k-1]])%N, k+1) + right[i][key[k-1]], 
                f((i-left[i][key[k-1]]+N)%N, k+1) + left[i][key[k-1]]) # 向右、向左
            return ans
        
        return f(0, 1)+M # 注意