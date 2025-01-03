"""
[hard]

给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。例如，如果 digits = ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。

返回 可以生成的小于或等于给定整数 n 的正整数的个数 。

 

示例 1：

输入：digits = ["1","3","5","7"], n = 100
输出：20
解释：
可写出的 20 个数字是：
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
示例 2：

输入：digits = ["1","4","9"], n = 1000000000
输出：29523
解释：
我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
81 个四位数字，243 个五位数字，729 个六位数字，
2187 个七位数字，6561 个八位数字和 19683 个九位数字。
总共，可以使用D中的数字写出 29523 个整数。
示例 3:

输入：digits = ["7"], n = 8
输出：1
 

提示：

1 <= digits.length <= 9
digits[i].length == 1
digits[i] 是从 '1' 到 '9' 的数
digits 中的所有值都 不同 
digits 按 非递减顺序 排列
1 <= n <= 109

https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/?source=vscode
"""

# 核心思路：数位dp

from functools import cache
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        N = len(s)
        @cache
        def f(r, is_limit, is_num):
            """返回总个数，当前到达第r位;0只能出现在开头"""
            if r == N: return 1

            ans = 0
            for i in range(len(digits)):
                if not is_limit or digits[i]<=s[r]:
                    ans += f(r+1, is_limit and digits[i]==s[r], True)
            
            if not is_num: # 单独开头的0
                ans += f(r+1, False, False)
            
            return ans
        return f(0, True, False)-1 # 减去全是0的情况
    
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        N = len(s)
        @cache
        def f(i, is_limit, pre_zero):
            """ """
            if N<=i: return 1
            ans = 0
            # 前导0的情况
            if pre_zero:
                ans += f(i+1, False, True)
            # 前导非0的情况
            for d in digits:
                if is_limit:
                    if d == s[i]:
                        ans += f(i+1, True, False)
                    elif d < s[i]:
                        ans += f(i+1, False, False)
                else:
                    ans += f(i+1, False, False)
                # ans += f(i+1, is_limit and , False) # 不好合并
            return ans

        return f(0, True, True)-1 # 减去0；默认情况下，也就是哨兵的情况下，前导为0