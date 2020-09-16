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


