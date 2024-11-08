"""
[hard]

可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。

 

示例 1：

输入：n = 2
输出：8
解释：
有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
示例 2：

输入：n = 1
输出：3
示例 3：

输入：n = 10101
输出：183236316
 

提示：

1 <= n <= 105

https://leetcode.cn/problems/student-attendance-record-ii/description/?source=vscode
"""

from functools import cache
N = 1_000_000_007
# 也就是结果会被缓存到全局存储表里面，这样调用 Solution().checkRecord()的时候，可以都从全局缓存表里面共享计算结果
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def f(n, cnt_a, c_l):
    """返回n，当前A个数cnt_a, 连续c_l个L时候的个数"""
    ans = 0
    if n == 1:
        ans = 1 # p
        if cnt_a < 1:
            ans += 1 # A
        
        if c_l < 2:
            ans += 1 # L
    else:
        ans += f(n-1, cnt_a, 0) # p
        if cnt_a < 1:
            ans += f(n-1, cnt_a + 1, 0) # A
        if c_l < 2:
            ans += f(n-1, cnt_a, c_l+1) # L
    return ans % N

class Solution:
    def checkRecord(self, n: int) -> int:
        return f(n, 0, 0)


    # 回溯：MLE
    def checkRecord_1(self, n: int) -> int:
        # ❌：如果写在里面，内存是过不了的
        # 原因：可以把 dfs 写在外面，这样多个测试用例之间可以共享记忆化搜索的结果，效率更高。
        """
        https://leetcode.cn/problems/student-attendance-record-ii/solutions/2885136/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-a8kj/?source=vscode
        """
        def f(n, cnt_a, c_l):
            """返回n，当前A个数cnt_a, 连续c_l个L时候的个数"""
            ans = 0
            if n == 1:
                ans = 1 # p
                if cnt_a < 1:
                    ans += 1 # A
                
                if c_l < 2:
                    ans += 1 # L
            else:
                ans += f(n-1, cnt_a, 0) # p
                if cnt_a < 1:
                    ans += f(n-1, cnt_a + 1, 0) # A
                if c_l < 2:
                    ans += f(n-1, cnt_a, c_l+1) # L
            return ans % N
        return f(n, 0, 0)
