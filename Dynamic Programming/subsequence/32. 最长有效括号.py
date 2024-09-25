"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号
子串
的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

https://leetcode.cn/problems/longest-valid-parentheses/description/?source=vscode
"""

# 难点：
#   状态表示、计算顺序

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 1:return 0
        # 状态表示 d[i] 表示 以 i 结尾的字符串最大长度
        d = [-1 for i in range(len(s))]

        # 对任意i，依赖i-1, i-2, i-2>=0, i>=2，因此初始化0，1
        d[0] = 0
        d[1] = 2 if (s[0] == '(' and s[1] == ')') else 0

        # 状态转移
        def f(s, i):
            # print(i)
            """
            求解s以i结尾的最长字符串个数
            对任意i，依赖i-1, i-2, i-2>=0, i>=2
            """
            if d[i] >= 0 :
                return d[i]
            
            ans = 0
            if i < 1:
                ans = 0
            elif s[i] == '(':
                ans = 0
            elif s[i] == ')':
                if s[i-1] == '(':
                    ans = f(s, i-2)+2
                else:
                    if i-f(s, i-1)-1 >=0 and s[i-f(s, i-1)-1] == '(':
                        ans = f(s, i-1) + 2
                        if i-f(s, i-1)-2 >=0:
                            ans += f(s, i-f(s, i-1)-2)
                    else:
                        ans = 0
            
            d[i] = ans

            return ans
        
        # 对任意i，依赖i-1, i-2, i-2>=0, i>=2，遍历从2开始
        for i in range(2, len(s)): 
            f(s, i)
        # print(d)
        return max(d)