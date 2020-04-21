'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        # 无小数
        if b == 0:
            return "".join(res)
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            # 在把该位置的记录下来
            loc[b] = len(res)
        return "".join(res)

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal/solution/ji-lu-yu-shu-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。