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

0 <= s.length <= 3 * 10^4
s[i] 为 '(' 或 ')'

https://leetcode.cn/problems/longest-valid-parentheses/description/?source=vscode
"""

# 难点：
#   状态表示、计算顺序

# 核心思路：
# 从数据规模上看 10^4，因此绝对只能涉及到一个变量，因此状态表示只能是 d[i]，因此必然是子序列问题，且在本题中为连续子序列
# 其次，比较有意思的一点是，将某个子问题的解，用来作为条件，判断括号是否成对
# 可以总结为，连续子序列的特殊类型问题的，特殊处理方式

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
    
    # method 1: 纯记忆化搜索
    def longestValidParentheses(self, s: str) -> int:
        # d[i]表示以i结尾的最长有效括号长度
        # 0<=i<N
        N = len(s)

        @cache
        def f(i):
            """表示以i结尾的最长有效括号长度"""
            nonlocal N
            # initialization
            if i==0: return 0
            if i==1: return 2 if s[:2] == '()' else 0

            # transition
            ans = 0
            if s[i] == '(':
                ans = 0
            elif s[i] == ')':
                if s[i-1] == '(':
                    ans = f(i-2)+2
                elif 0<=i-f(i-1)-1 and s[i-f(i-1)-1] == '(':
                    ans = f(i-1)+2+(f(i-f(i-1)-2) if 0<=i-f(i-1)-2 else 0)
            
            return ans
        ans = [0]
        for i in range(N):
            ans.append(f(i))
        return max(ans)