"""
[medium]

给你一个字符串 word 和一个整数 numFriends。

Alice 正在为她的 numFriends 位朋友组织一个游戏。游戏分为多个回合，在每一回合中：

word 被分割成 numFriends 个 非空 字符串，且该分割方式与之前的任意回合所采用的都 不完全相同 。
所有分割出的字符串都会被放入一个盒子中。
在所有回合结束后，找出盒子中 
字典序最大的 
字符串。

 

示例 1：

输入: word = "dbca", numFriends = 2

输出: "dbc"

解释: 

所有可能的分割方式为：

"d" 和 "bca"。
"db" 和 "ca"。
"dbc" 和 "a"。
示例 2：

输入: word = "gggg", numFriends = 4

输出: "g"

解释: 

唯一可能的分割方式为："g", "g", "g", 和 "g"。

 

提示:

1 <= word.length <= 5 * 103
word 仅由小写英文字母组成。
1 <= numFriends <= word.length

"""

# 核心思路：
# ❌方案1: 很容易想到用01背包，但是状态不成立，无法写出状态转移
# 方案2: 贪心
"""
为什么能够想到贪心：
    首先由解的完备性知道，解一定是全局最优解
    暴力解 -> 必然可以通过某些性质（本题中为贪心）来优化 -> 降低复杂度
"""


class Solution:

    # 贪心：O(N^2)
    """
    如果固定子串的左端点，那么子串越长，字典序越大。
    所以核心思路是：枚举子串的左端点，计算最大子串。
    """
    def answerString(self, s: str, k: int) -> str:
        if k == 1:
            return s
        n = len(s)
        return max(s[i: i + n - k + 1] for i in range(n))
    
    def answerString(self, word: str, numFriends: int) -> str:
        # 由贪心知最优解一定在 max([s[i:i+n-k+1] for i in range(n)])中
        # 因此直接找出所有最大后缀，然后取其前缀s[l:l+n-k+1]即为答案
        l, r, d = 0, 1, 0
        s = word
        k = numFriends
        n = len(s)

        if numFriends == 1: return s

        while r+d<n:
            if s[l+d] == s[r+d]:
                d += 1
            else:
                if s[l+d] < s[r+d]:
                    l += d + 1
                else:
                    r += d + 1
                d = 0
                r = max(r, l+1)
        return s[l:l+n-k+1]


if __name__ == "__main__":
    res = Solution().answerString(
        "aaaao",
        4
    )