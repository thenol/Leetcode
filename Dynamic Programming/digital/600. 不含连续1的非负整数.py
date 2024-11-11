"""
[hard]

给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。

 

示例 1:

输入: n = 5
输出: 5
解释: 
下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。
示例 2:

输入: n = 1
输出: 2
示例 3:

输入: n = 2
输出: 3
 

提示:

1 <= n <= 109

https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/description/?source=vscode
"""

# 核心思路：数位dp
"""
模板：
https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/solutions/1750941/by-endlesscheng-1egu/?source=vscode
"""

from functools import cache
class Solution:
    def findIntegers_1(self, n: int) -> int:
        """简单写法"""
        @cache
        def f(i, pre, is_limit):
            """表示当前进行到了第i位，前面是否有1，当前是否受限的个数；0<=i<n"""
            if i < 0:
                return 1
            up = (n >> i) & 1 if is_limit else 1 # 判断当前数位的上界
            ans = 0
            for d in range(up + 1): # 遍历数位
                #如果前面为1，同时当前打算填1，是不行的
                if pre and d == 1: # 如果前一位为1，当前也为1，跳过，因为不允许存在连续1
                    continue
                ans += f(i - 1,d == 1,is_limit and d == up) # 当前受限，当且仅当 当前受限 且 到达遍历数位上界时
            return ans
        return f(n.bit_length(),False,True) # 注意当n=10(二进制1010)时，n>>4=0

    # 复杂写法
    def findIntegers(self, n: int) -> int:
        # 数型dp
        # method 1: 转换成字符串来做dp；比较trick
        s = str(bin(n)).lstrip("0b")
        N = len(s)

        # 计算的时候，可以先少算一位，最后在前面加一个0或者1，这样简化和s判断大小的复杂度
        # 5 = 101
        @cache 
        def f(cur, free, cnt):
            """
            表示
            cur 当前第几位
            free 当前是否可以随便填写0和1
            cnt 当前连续1的个数
            的个数
            """
            if cur == N-1: # cur从0出发，毫无疑问判断右边界
                if free:
                    if cnt == 1: return 1 # 只能填0
                    if cnt == 0: return 2 # 可以填0或1
                else:
                    if s[cur] == '0': return 1 # 只能填0
                    elif s[cur] == '1':
                        if cnt == 1: return 1 # 只能填0
                        if cnt == 0: return 2 # 可以填0或1

            if free: # 后面都可以随便填写，只受cnt控制
                if cnt == 1: return f(cur+1, 1, 0) # 只能填0
                if cnt == 0: return  f(cur+1, 1, 0) + f(cur+1, 1, 1) # 可以填0或1
            else: # 后面可能free，也可能不free
                if s[cur] == '0': return f(cur+1, 0, 0) # 只能填0，还是不free
                elif s[cur] == '1':
                    if cnt == 1: return f(cur+1, 1, 0) # 只能填0，free
                    if cnt == 0: return f(cur+1, 1, 0) + f(cur+1, 0, 1) # 可以填0或1

        return f(0, 0, 0)