"""
[medium]

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
"""

# 状态思路：关注每一个item，状态一定和item有关系，必然是d[i][j] => 其次思考，在这个点的时候，要想计算出最大正方形，所需要的充要条件是什么，这个就是状态

class Solution:
    # method 2: 迭代法
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # state: d[i][j]表示以i,j为右下角的最大正方形边长
        # 0<=i<R;0<=j<C
        R, C = len(matrix), len(matrix[0])

        # initialization
        d = [[int(matrix[i][j]) for j in range(C)] for i in range(R)]

        # transition
        ans = 0
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == '0':
                    d[i][j] = 0
                elif 0<=i-1 and 0<=j-1: # 归约态已经ready，只需找成功转移
                    later = min(d[i-1][j], d[i][j-1])
                    if matrix[i-later][j-later] == '1':
                        later += 1
                    d[i][j] = later
                    
                ans = max(ans, d[i][j])
        
        # print(d)
        return ans*ans
    
    # method 1: 挂表法
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # state: d[i][j] 表示以matrix[i][j]为右下角的正方形的边长; 0<=i<len(matrix), 0<=j<len(matrix[0])
        d = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        # initialization;0<=i, 0<=j
        # j==0
        for i in range(len(matrix)):
            d[i][0] = 1 if matrix[i][0] == '1' else 0
        
        for j in range(len(matrix[0])):
            d[0][j] = 1 if matrix[0][j] == '1' else 0

        # print(d)
        # transition
        def f(i, j):
            """
            以matrix[i][j]为右下角的正方形的边长
            条件：1<=i, 1<=j
            """
            if d[i][j] >= 0:
                return d[i][j]
            
            # 当前为0，则不可能组成正方形
            if matrix[i][j] == '0':
                return 0
            
            # 当前为1，继续合并正方形
            ans = 0
            later = min(f(i-1, j), f(i,j-1))
            if later == 0:
                ans = 1
            elif matrix[i-later][j-later] == '0':
                # 边存在，一定不会越界
                ans = later #易错点❌，要学会验算，而不是想当然
            else:
                ans = later + 1
            
            d[i][j] = ans # 易错点❌：这是挂表法的模板啊，就是死记硬背也要记住啊，要形成肌肉记忆
            return d[i][j]
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, f(i,j))
        # print(d)
        return ans**2