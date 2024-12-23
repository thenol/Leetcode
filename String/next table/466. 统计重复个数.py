"""
[hard]

定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。

例如，str == ["abc", 3] =="abcabcabc" 。
如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。

例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。

请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。

 

示例 1：

输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
输出：2
示例 2：

输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
输出：1
 

提示：

1 <= s1.length, s2.length <= 100
s1 和 s2 由小写英文字母组成
1 <= n1, n2 <= 106


https://leetcode.cn/problems/count-the-repetitions/description/?source=vscode

"""

# 核心思路：预处理next搜索位置
# 本质：通过预处理，直接找到了下一次匹配的位置，从而实现跳跃性的匹配加速，大大提升效率，降低复杂度
"""
最佳答案：

我们预处理出以字符串 s2 的每个位置 i 开始匹配一个完整的 s1 后，下一个位置 j 以及经过了多少个 s2，即 d[i]=(cnt,j)，其中 cnt 表示匹配了多少个 s2，而 j 表示字符串 s2 的下一个位置。

https://leetcode.cn/problems/count-the-repetitions/solutions/2587504/python3javacgotypescript-yi-ti-yi-jie-yu-n84j/?source=vscode

  a c b --- a c b
  a   b --- a
j:0   1 --- j=0, cnt=1
"""

from collections import Counter
class Solution:
    # 时间复杂度 O(m×n+n1)，空间复杂度 O(n)
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        n = len(s2)
        d = {}
        for i in range(n):
            cnt = 0
            j = i
            for c in s1: # j标定了从i出发，匹配了cnt个s2之后 s2 中的位置
                if c == s2[j]:
                    j += 1
                if j == n:
                    cnt += 1
                    j = 0
            d[i] = (cnt, j) # 构建跳表，用于后续决策：遍历一个完整的s1，得知从i出发之后，可以经过循环匹配 cnt 个 s2 之后，匹配到 s2 的 j 位置；因此，再从头开始遍历匹配s1时，就应该从j开始

        ans = 0
        j = 0
        for _ in range(n1): # s1循环 n1 次，s2先从0开始遍历，从而由d得到，经过循环遍历 cnt 个 s2 之后下一次从j开始继续匹配
            cnt, j = d[j] 
            ans += cnt
        return ans // n2

    # MLE: Memory Limit Exceeded
    def getMaxRepetitions_1(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # state: 
        def derive(str1, str2):
            """str2可以从str1获得，删str1获得str2"""
            # state: d[i][j]表示str2[:j]可以由str1[:i]获得，注意末尾字符对应分别为str2[j-1]，str1[i-1]
            # 0<=i<=len(str1); 0<=j=len(str2)
            M = len(str1)
            N = len(str2)
            d = [[False for j in range(N+1)] for i in range(M+1)]

            # initialization
            # 1<=i;1<=j
            # str2=''
            for i in range(M+1):
                d[i][0] = True
            
            # str1=''
            for j in range(N+1):
                d[0][j] = False
            
            d[0][0] = True

            # transition
            # 1<=i;1<=j
            for i in range(1, M+1):
                for j in range(1, N+1):
                    if str1[i-1] == str2[j-1]:
                        # 末尾匹配，j可能由i前面的字符匹配，也可能由当前i的字符匹配
                        d[i][j] = d[i-1][j-1] or d[i-1][j]
                    else:
                        # 末尾不匹配，只能j只能由i前面的字符匹配
                        d[i][j] = d[i-1][j]
            
            return d[M][N]

        str1 = s1*n1
        str2 = s2*n2
        cnt = Counter(str1)
        mx_m = max(cnt.values())
        for i in range(mx_m, -1, -1):
            if derive(str1, str2*i):
                return i
