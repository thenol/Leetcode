"""
[medium]

返回 s 字典序最小的
子序列
，该子序列包含 s 的所有不同字符，且只包含一次。

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 1000
s 由小写英文字母组成
 

注意：该题与 316 https://leetcode.cn/problems/remove-duplicate-letters/ 相同
"""

class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            # 已经出现的字符，就不用增加了，
            # 原因：对于新增加的字符，即使入栈，影响的也是该字符及其之后的字符，因为出栈的只会是不高于当前字符的字符
            # 如果把该字符增加过来，后面新增加的不一定会比当前形成的字符序列更小，即使有和当前形成的字符序列相同大小的字符序列，随着后面的进行，也不至于形成比当前更小的字符序列
            if c not in stack: 
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
