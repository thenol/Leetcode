"""
[medium]

给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
 

示例 1：

输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
示例 2：

输入：n = 0
输出：1
 

提示：

0 <= n <= 8

https://leetcode.cn/problems/count-numbers-with-unique-digits/description/?source=vscode
"""

class Solution:
    # digitial dynamic programming
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def f(i, pre):
            """
            当前第i位，已经选择了pre状态中所有数的情况下的种数
            例如 i=1, pre=01 0000 0000 选择了1
            """
            if i == n: return 1 # 选择到了第n个数了，最后只剩1种了
            ans = 1 # 凡是能选到当前位i的，必然说明i没选择过，因此这一位肯定可以选择 i，即起码1种，也就是到当前位为止是一种情况

            # 继续按照可能性拼接后续位数
            for d in range(10):
                # pre==0 and d==0: 当前还未选择数且第一位为0，也就是先导0 情况跳过
                # pre当前已经被选择过了跳过
                if (pre == 0 and d == 0) or pre >> d & 1:
                    continue
                ans += f(i+1, pre ^ (1<<d))
            return ans
        
        return f(0, 0) # 刚开始i=0表示没选择，且pre已经选择的位空集，即状态为 00 0000 0000

    # math version: 排列组合
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # state: d[i]表示0<=x<10^i
        if n==0: return 1
        if n==1: return 10
        acc, ans = 9, 10
        for i in range(n-1):
            acc *= 9-i
            ans += acc
        return ans

    # TLE version
    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        def duplicated(s):
            ans = False
            pre = set()
            for c in s:
                if c in pre:
                    return True
                else:
                    pre.add(c)
            return ans
        
        cnt = 0
        for i in range(10**n):
            if duplicated(str(i)):
                continue
            else:
                cnt += 1
        return cnt