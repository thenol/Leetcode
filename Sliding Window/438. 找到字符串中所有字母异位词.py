"""
[medium]

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母

https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
"""

from collections import Counter
class Solution:
    # 固定窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt_s = Counter()
        stk = []
        ans = []
        for i, c in enumerate(s):
            while stk and len(stk) >= len(p):
                cnt_s[stk.pop(0)] -= 1
            stk.append(c)
            cnt_s[c] += 1
            if cnt_s == cnt_p: # Counter元素可以直接相比
                ans.append(i - len(p)+1)
        
        return ans
    
    # method 2: 可变窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数；剩余窗口字符集
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans

        