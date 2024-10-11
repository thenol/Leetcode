"""[hard]
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 

提示：

1 <= s.length <= 20
1 <= p.length <= 20
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符

https://leetcode.cn/problems/regular-expression-matching/description/
"""
# 思路1: 动态规划，填表法，哨兵控制边界
# 总结：字符串类型处理的特殊技巧:
#   1. 状态表示d[i][j]表示，以i，j结尾
#   2. 状态转移方程，从字符串末尾，也就是右侧开始向左⬅️处理
"""
难点：1.边界控制；2.分类讨论；3.字符串从右往左（如果从左往右，需要考虑前一个状态，可以看一下思路2）
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        ## 状态表示 & 初始化
        # !!! 状态表示：dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自 前 i、j 个是否匹配
        # 注意细节 dp[i][j] 对应判断的字符串分别是 s[i-1], p[i-1]
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        
        ## 边界处理 ++++++++++++++++++++++++++++++++++++++++++++++++
        dp[0][0] = True # 空串自然相互匹配

        # s 为空串
        for j in range(1, p_len + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 个可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        ## 边界处理 ++++++++++++++++++++++++++++++++++++++++++++++++

        ## 状态转移方程
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] in {s[i - 1], '.'}: # 如果 p[j-1] 和 s[i-1] 匹配，2种情况
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*': # 如果 p[j-1] 和 s[i-1] 不匹配 且 p[j - 1] == '*'，开始拯救，3种情况
                    if p[j - 2] in {s[i - 1], '.'}: # 看 p[j - 2] 和 s[i-1] 是否匹配，如果匹配
                        dp[i][j] = dp[i][j - 2] or dp[i-1][j - 2] or dp[i - 1][j] # 分别对应 * 为 0次、1次、2次及以上
                    else: # p[j - 2] 和 s[i-1] 是否匹配，如果不匹配，必须消耗一个*
                        dp[i][j] = dp[i][j - 2]
        return dp[s_len][p_len]

# https://leetcode.cn/problems/regular-expression-matching/solutions/296114/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/
    

"""
展开：
if a==b or a==c

简化：
if a in {b, c}
"""


# 思路1：记忆化搜索 边界情况不好判定，在这里附上错误的case!!!
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, True)
    
    @lru_cache
    def dfs(self, s, i, p ,j, last=True):
        print(i,j)
        # if i==len(s)-1 and j == len(p)-1 and s[i] == p[j]:return True
        # if (i < len(s) and j >=len(p)) or (i < len(s) and j >=len(p)):return False
        if i < len(s) and j>=len(p): return False
        if i == len(s):
            if j == len(p) - 1 and p[j] == '*':
                return True and last
            elif j == len(p):
                return True and last
            elif j == len(p)-2 and p[j+1] == '*':
                return True and last
            else:
                return False

        if p[j] == '.':
            return last and self.dfs(s, i+1, p, j+1, True)
        if p[j] == '*':
            return (self.dfs(s, i, p, j+1, True) or self.dfs(s, i, p, j-1, True)\
            or self.dfs(s, i-1, p, j+1, True)) if last else self.dfs(s, i, p, j+1, False)
        if s:
            if s[i]==p[j]:
                return self.dfs(s, i+1, p, j+1, True)
            else:
                return self.dfs(s, i, p, j+1, False)

        return False

        
# 思路1: 记忆化搜索
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # state definition
        # d[i][j] denotes s[:i] and p[:j] match or not

        # boundary initialization
        d = [[ -1 for j in range(len(p)+1)] for i in range(len(s)+1)]
        ## when s == '' and p == ''
        d[0][0] = 1
        ## when p == ''
        for i in range(1, len(s)+1):
            d[i][0] = 0
        ## when s == ''
        for j in range(1, len(p)+1):
            d[0][j] = 0
            if p[j-1] == "*": ## p[0] mustn't be *, otherwise the string is illegal
                d[0][j] = d[0][j-2]
        
        # state transition
        def f(s, p, i, j):
            """
            s[:i] and p[:j] match or not
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            ans = 0
            if p[j-1] == '.':
                ans = f(s, p, i-1, j-1)
            elif p[j-1] == '*':
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    """
                    * match 0, 1, 2 times
                    """
                    ans = f(s, p, i, j-2)\
                        or f(s, p, i-1, j-2)\
                            or f(s, p, i-1, j)
                else:
                    ans = f(s, p, i, j-2)
            else:
                ans = (s[i-1]==p[j-1]) and f(s, p, i-1, j-1)
            
            d[i][j] = ans
            return d[i][j]
        
        f(s, p, len(s), len(p))

        return bool(d[len(s)][len(p)])
    