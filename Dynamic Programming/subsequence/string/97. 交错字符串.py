'''
[medium]
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 
子字符串
：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

 

示例 1：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true
 

提示：

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
 

进阶：您能否仅使用 O(s2.length) 额外的内存空间来解决它?

https://leetcode.cn/problems/interleaving-string/description/
'''
# 思路：
"""
【状态选择】：
方式1: 根据题意看着容易想着用s1[i:j], s2[k:h], s3[x:y]来表示 s3[x:y]是否可以由s1[i:j], s2[k:h]交错表示关系。但是这种方法，一方面表示起来涉及到6个变量，比较麻烦，不好写转移方程

方式2（最优解表示）: s1[:i],s2[:j],s3[:k]，用来表示s3[:k]是否可以由s1[:i],s2[:j]交错表示关系。这种方法只涉及到3个变量，方便写状态转移方程

【状态转移方程】：
很简单，类比子串匹配 f(i,j,k) = (f(i, j-1, k-1) if s3[k-1] == s2[j-1]) or (f(i-1, j, k-1) if s3[k-1] == s1[i-1])

【初始化状态】：易错点❌
注意变量范围：1<=i<=len(s1),1<=j<=len(s2),1<=k<=len(s3)，因此需要初始化三种边界情况
1. s2=""，0<=j
2. s1=""，0<=i
3. s3=""，0<=k
4. 特殊照顾情况 d[0][0][0] = 1

注意不能从1开始遍历初始化，否则会漏掉很多[0][j][k]的情况
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # state: d[i][j][k] 表示s3[:k]是否可以由s1[:i],s2[:j]交错而成, 0<=i<=len(s1),0<=j<=len(s2),0<=k<=len(s3)
        d = [[[-1 for k in range(len(s3)+1)] \
            for j in range(len(s2)+1)] for i in range(len(s1)+1)]

        # intialization
        # 1<=i<=len(s1),1<=j<=len(s2),1<=k<=len(s3)
        
        # s2=""，0<=j
        for i in range(len(s1)+1):
            for k in range(len(s3)+1):
                d[i][0][k] = int(s1[:i] == s3[:k])
        
        # s1=""，0<=i
        for j in range(len(s2)+1):
            for k in range(len(s3)+1):
                d[0][j][k] = int(s2[:j] == s3[:k])
        
        # s3=""，0<=k
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                d[i][j][0] = 0
        
        d[0][0][0] = 1

        
        # transition
        def f(i, j, k):
            """
            d[i][j][k] 表示s3[:k]是否可以由s1[:i],s2[:j]交错而成
            1<=i<=len(s1),1<=j<=len(s2),1<=k<=len(s3)
            """
            if d[i][j][k] >= 0:
                return d[i][j][k]
            
            ans = 0
            if s3[k-1] == s2[j-1]:
                ans = f(i, j-1, k-1)
            if s3[k-1] == s1[i-1]:
                ans = int(ans or f(i-1, j, k-1))

            d[i][j][k] = ans
            return d[i][j][k]
        
        f(len(s1), len(s2), len(s3))
        return bool(d[len(s1)][len(s2)][len(s3)])
