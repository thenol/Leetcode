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
"""
最佳答案：
https://leetcode.cn/problems/count-the-repetitions/solutions/2587504/python3javacgotypescript-yi-ti-yi-jie-yu-n84j/?source=vscode
"""

from collections import Counter
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """可以用kimi解释题目和代码并且添加注释"""
        # 计算s2的长度，用于确定循环的边界
        n = len(s2)
        # 初始化一个字典，用于存储中间状态
        d = {}
        
        # 外层循环遍历s2的每个字符，构建中间状态
        for i in range(n):
            cnt = 0  # 计数器，记录s2在s1中出现的次数
            j = i  # j是s2的索引，用于记录当前匹配的位置
            # 内层循环遍历s1的每个字符，与s2进行匹配
            for _ in range(n1):  # 这里使用_作为占位符，因为我们不关心s1的具体字符
                si = s1  # 临时变量，存储s1的当前状态
                # 遍历s1，寻找与s2匹配的字符
                for c in si:
                    if c == s2[j]:  # 如果s1的字符与s2的当前字符匹配
                        j += 1  # 移动s2的索引
                    if j == n:  # 如果j到达s2的末尾，说明找到了一个完整的s2
                        cnt += 1  # 计数器加1
                        j = 0  # 重置j，开始寻找下一个s2
            # 将当前索引i对应的s2的完整匹配次数cnt和下一个搜索的起始索引j存储在字典d中
            d[i] = (cnt, j)

        # 初始化ans，用于存储最终答案
        ans = 0
        j = 0  # 重置j为0，从s2的开头开始搜索
        # 外层循环遍历n1次，每次循环代表s1的一次完整遍历
        for _ in range(n1):
            # 从字典d中获取当前索引j对应的匹配次数cnt和下一个搜索的起始索引j
            cnt, j = d[j]
            ans += cnt  # 将找到的s2的次数累加到ans中

        # 返回ans除以n2的结果，即str2重复的最大次数m
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
