"""
[hard]

使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。

 

示例 1：

输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
示例 2：

输入：s1 = "abcde", s2 = "caebd"
输出：false
示例 3：

输入：s1 = "a", s2 = "a"
输出：true
 

提示：

s1.length == s2.length
1 <= s1.length <= 30
s1 和 s2 由小写英文字母组成

https://leetcode.cn/problems/scramble-string/description/
"""

# 思路：
"""
1. 状态判定：
    为什么只能用d[i][j][k][h] 而不能用 d[i] ？

    因为d[i]只能表示成s1[:i]扰乱成s2[:i]也就是只能顺序扰乱，没办法表示字符串 s1[i:j] 扰乱成 s2[k:h]，这是显然不符合题意的

2. 状态转移方程：
    注意仔细阅读题意，不管对s1做何种扰乱，任何一个子树的根节点都是不变的，本质上其实就是一棵树在不断的更换自己的左右子树，但是左右子树内部关系相互独立
    
    因此如果使 d[i][j][k][h] 成立，就一定存在 g 使得 d[i][g][k][g]和d[g][j][g][h]成立成立 或者 d[i][g][g][h]和d[g][j][k][g]成立，即：

    【拆分成子问题的依据】
    d[i][j][k][h]成立的必要条件：

    d[i][j][k][h] = (d[i][g][k][g] and d[g][j][g][h]) or 
                    (d[i][g][g][h] and d[g][j][k][g])
    
    【转换成三维】
    d[i][j][len]
"""

from functools import cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        # state: d[i][j][k][h] 表示s1[i:j]是否可以扰乱成s2[k:h]
        # 状态简化 d[i][j][len] 表示s1[i:i+len]是否可以扰乱成s2[j:j+len]
        # 0<=i, 0<=j, 0<=le<=len(s)
        d = [[[-1 for k in range(len(s1)+1)]for j in range(len(s1))]for i in range(len(s1))]

        # initialization
        # k-i>=1恒成立，只需初始化i=0,j=0,len=1
        for i in range(len(s1)):
            for j in range(len(s2)):
                d[i][j][1] = int(s1[i:i+1] == s2[j:j+1])
        
        for i in range(len(s1)):
            d[0][i][0] = 1
            d[i][0][0] = 1
        
        # 特殊值debug
        # print(d[0][0][1], d[0][1][1], d[1][0][1], d[0][1][1])

        def f(s1, s2, i, j, le):
            """
            表示s1[i:i+le]是否可以扰乱成s2[j:j+le]
            下标范围：[i,...,i+le-1]
            d[i][j][le]依赖  k-i>=1恒成立, i>=0, j>=0
            """
            if d[i][j][le] >= 0:
                return d[i][j][le]
            
            ans = 0
            if s1[i:i+le] == s2[j:j+le]:
                ans = 1
            else:
                for k in range(i+1, i+le): # k的取值范围[i,...,i+le-1]
                    # 以k为拆分点，拆分成子串[i:k],[k:i+le]
                    if (f(s1, s2, i, j, k-i) and f(s1, s2, k, j+k-i, le-k+i)) \
                        or (f(s1, s2, i, j+le-k+i, k-i) and f(s1, s2, k, j, le-k+i)):
                        ans = 1
                        break
                
            d[i][j][le] = ans
            return ans

        f(s1, s2, 0, 0, len(s1))
        # print(d)
        return bool(d[0][0][len(s1)])

    # 纯记忆化搜索
    def isScramble(self, s1: str, s2: str) -> bool:
        # state: d[i][j][k] 表示s1[i-k:i]翻转s2[j-k:j]
        # 0<=i<=N; 0<=j<=N; 0<=k<=N
        N = len(s1)
        M = len(s2)
        if N!=M: return False
        @cache
        def f(i, j, k):
            """表示表示s1[i-k:i]翻转s2[j-k:j]"""
            nonlocal s1, s2, N
            # initialization
            if i-k<0 or j-k<0: return False
            if s1[i-k:i] == s2[j-k:j]: return True

            # transition
            ans = False
            for l in range(1, k):
                ans = ans or (f(i, j, l) and f(i-l, j-l, k-l)) or (f(i-k+l, j, l) and f(i, j-l, k-l))
            return ans
        
        return f(N, N, N)