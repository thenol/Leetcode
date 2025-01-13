"""
[hard]

给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。

 

示例 1：

输入：s = "abab"
输出："bab"
解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
示例 2：

输入：s = "leetcode"
输出："tcode"
 

提示：

1 <= s.length <= 4 * 105
s 仅含有小写英文字符。

https://leetcode.cn/problems/last-substring-in-lexicographical-order/description/

"""


# 核心思路：
#   需要能看出贪心策略，即 当字符串 s 中的子串开始下标确定时，子串的长度越大，其字典序越大，因此字符串 s 的所有子串中字典序最大的子串一定是字符串 s 的一个「后缀」。
"""
最佳答案：
https://leetcode.cn/problems/last-substring-in-lexicographical-order/solutions/1792643/by-stormsunshine-zsgp/
"""

class Solution:
    # MLE; O(N^2)
    def lastSubstring(self, s: str) -> str:
        return max([s[i:] for i in range(len(s))])
    

    def lastSubstring(self, s: str) -> str:
        N = len(s)
        l, r, d = 0, 1, 0 # l记录最大后缀字符串的开始位置，r记录下一个比较大为主

        while r+d<N:
            if s[l+d] == s[r+d]: # 如果相同，继续比较
                d += 1
            else:
                if s[l+d] < s[r+d]: # 否则，如果s[r+d]更大，则意味着对于 l<=d'<=d，则s[l+d':l+d]<s[r+d':r+d]
                    l += d + 1
                else: # 同上
                    r += d + 1
                d = 0 # 重新比较
                r = max(r, l+1) # l更新之后，l之前都比较都没有意义，一定都小于s[l:]，因为 s[l:]标志着最大后缀字符串的开始，所以当 r<l 时，一定比s[l:]小，所以直接更新 r
        
        return s[l:]
            
        