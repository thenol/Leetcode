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
