"""
[medium]

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的
字典序
最小（要求不能打乱其他字符的相对位置）。

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成
"""

# 思路：
"""
https://leetcode.cn/problems/create-maximum-number/solutions/297892/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-7/?source=vscode
"""

from collections import Counter
import itertools
class Solution:
    # 很差的代码——删除的思路
    def removeDuplicateLetters1(self, s: str) -> str:
        counter = Counter(list(itertools.chain(s)))
        stk = []
        for c in s:
            if c not in stk:
                while stk and c < stk[-1] and counter[stk[-1]]>1:
                    counter[stk[-1]] -= 1
                    stk.pop()
                stk.append(c)
            else:
                counter[c] -= 1
        
        return "".join(stk)
    
    # ✅ 优雅版本代码——挑选的思路
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        remain_counter = Counter(s)

        for c in s:
            if c not in stk:
                while stk and c < stk[-1] and remain_counter[stk[-1]] > 0:
                    stk.pop()
                stk.append(c)
            remain_counter[c] -= 1
        
        return "".join(stk)

