'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 方法一：挂表法
# 思路：
"""
【状态表示】：
d[i][j] 表示 s[:i]子序列存在t[:j]的个数

【转移方程】：
...

【初始化】：
注意这里可以从1开始初始化的原因，可以对比一下三维动态规划，例如《97.交错字符串.py》


"""
class Solution:
    # 01背包——记忆化搜索
    def numDistinct(self, s: str, t: str) -> int:
        # state: d[i][j]表示s[:i]范围可以形成t[:j]的方案数
        # 0<=i<=N; 0<=j<=M
        N, M = len(s), len(t)
        @cache
        def f(i, j):
            """表示s[:i]范围可以形成t[:j]的方案数"""
            nonlocal N, M

            # initialization
            if j==0: return 1 # 找到了一种；归约态是一个集合

            # transition
            ans = 0
            if 1<=i and 1<=j and s[i-1] == t[j-1]:
                ans += f(i-1, j-1) + f(i-1, j)
            elif 1<=i:
                ans += f(i-1, j)
            
            return ans
        
        return f(N, M)

    def numDistinct(self, s: str, t: str) -> int:
        # state: d[i][j] 表示s[:i]中可以找到的t[:j]的表示个数
        # 0<=i<=len(s), 0<=j<=len(t)
        d = [[-1 for j in range(len(t)+1)] for i in range(len(s)+1)]

        # initialization
        d[0][0] = 1

        # s=""，可以从1开始，
        for j in range(1, len(t)+1):
            d[0][j] = 0
        
        # t=""
        for i in range(1, len(s)+1):
            d[i][0] = 1


        def f(i, j):
            """
            d[i][j] 表示s[:i]中可以找到的t[:j]的表示个数
            0<=i<=len(s), 0<=j<=len(t)
            依赖：1<=i,j
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            ans = 0
            if i < j:
                ans = 0
            elif s[i-1] == t[j-1]:
                ans = f(i-1, j-1) + f(i-1, j)
            else:
                ans = f(i-1, j)
            
            d[i][j] = ans
            return d[i][j]
        
        f(len(s), len(t))
        return d[len(s)][len(t)]


# 方法2: 刷表法
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dynamic programming
        # from top to bottom:
        # initialization
        m=len(s)
        n=len(t)
        if not s or m<n:
            return 0
        d=[[0 for _ in range(n)] for _ in range(m)]
        d[0][0]=1 if s[0]==t[0] else 0
        for i in range(1,m):
            d[i][0]=d[i-1][0]+1 if s[i]==t[0] else d[i-1][0] # Note the initialization without additional ordinary boundary!!!
        for i in range(1,m):
            for j in range(1,n):
                if s[i]==t[j]:
                    d[i][j]=d[i-1][j-1]+d[i-1][j] # !!!Note there will be duplicated situation if plus 1 (i.e. error: d[i][j]=d[i-1][j-1]+d[i-1][j]+1)
                else:
                    d[i][j]=d[i-1][j]
        
        return d[m-1][n-1]
    


    # Pay attention to the benefits of this method, and if you do n’t follow this method, pay attention to the problems during initialization
    '''
    class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]

    作者：powcai
    链接：https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-by-powcai-5/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
