'''
[hard]
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from math import inf
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # S: d[i][j] as the minimum value
        # E:
        # if word1[i]==word2[j]:d[i][j]=d[i-1][j-1]
        # else:d[i][j]=min(d[i-1][j],d[i][j-1],d[i-1][j-1])+1 # delete, insert, replace
        # I: i,
        d=[[0 for _ in range(len(word2)+1)]for _ in range(len(word1)+1)]

        # version 1: 初始化容易出错，一下为错误版本
        # for i in range(len(word1)):
        #     if word2[0]==word1[i]:
        #         d[i][0]=i
        #     else:
        #         d[i][0]=i+1
        # for i in range(len(word2)):
        #     if word2[i]==word1[0]:
        #         d[0][i]=i
        #     else:
        #         d[0][i]=i+1

        # version 2: 包含空串初始化操作
        for i in range(1,len(word1)+1):
            d[i][0]=d[i-1][0]+1 # 把空串""放进来初始化，会大大地简化问题
        for i in range(1,len(word2)+1):
            d[0][i]=d[0][i-1]+1 # 把空串""放进来初始化，会大大地简化问题
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:d[i][j]=d[i-1][j-1]
                else:d[i][j]=min(d[i-1][j],d[i][j-1],d[i-1][j-1])+1
        print(d)
        return d[-1][-1]


class Solution:
    # 记忆化搜索+挂表
    def minDistance(self, word1: str, word2: str) -> int:
        # state: d[i][j] 表示 word1[:i],编辑到word2[:j]所需要的最小操作数
        # 0<=i<=len(word1), 0<=j<=len(word2)
        d = [[-1 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

        # initialization
        # d[i][j] 依赖 i-1, j-1, so i>=1, j>=1, 初始化 0边界
        d[0][0] = 0

        # word2=""
        for i in range(1, len(word1)+1):
            d[i][0] = i
        
        # word1=""
        for j in range(1, len(word2)+1):
            d[0][j] = j
        
        # transition
        def f(word1, word2, i, j):
            """
            表示 word1[:i],编辑到word2[:j]所需要的最小操作数
            0<=i<=len(word1), 0<=j<=len(word2)
            依赖 i-1, j-1, so i>=1, j>=1
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            ans = 0
            if word1[i-1] == word2[j-1]:
                ans = f(word1, word2, i-1, j-1)
            else:
                ans = min(
                    f(word1, word2, i-1, j-1) + 1, # 替换
                    f(word1, word2, i, j-1) + 1, # 插入
                    f(word1, word2, i-1, j) + 1, # 删除
                    )
            d[i][j] = ans

            return ans
        
        f(word1, word2, len(word1), len(word2))

        return d[len(word1)][len(word2)]
    
    # 纯记忆化搜索
    # 多归约状态
    # ❗️❗️❗️：别忘了记忆化搜索状态初始化和迭代法必须完完全全相同啊，否则遗漏必错❗️❗️❗️
    def minDistance(self, word1: str, word2: str) -> int:
        # state: d[i][j]表示将word1[:i]编辑成word2[:j]需要的最小操作数
        # 0<=i<=N; 0<=j<=M
        N, M = len(word1), len(word2)
        @cache
        def f(i, j):
            """表示将word1[:i]编辑成word2[:j]需要的最小操作数"""
            nonlocal N, M, word1, word2
            # initialization
            if i==0 and j==0: return 0 # 不需要操作
            if i==0: return j # word1为空时
            if j==0: return i # word2 为空时

            # transition
            ans = inf
            if word1[i-1] == word2[j-1]:
                ans = min(ans, f(i-1, j-1))
            else:
                ans = min(
                    ans, 
                    f(i, j-1)+1, # 插入一个字符 
                    f(i-1, j)+1, # 删除一个字符
                    f(i-1, j-1)+1, # 替换一个字符
                    )
            
            return ans
        return f(N, M)