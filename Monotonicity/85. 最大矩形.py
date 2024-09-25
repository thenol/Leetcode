"""
[hard]
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = [["0"]]
输出：0
示例 3：

输入：matrix = [["1"]]
输出：1
 

提示：

rows == matrix.length
cols == matrix[0].length
1 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

https://leetcode.cn/problems/maximal-rectangle/description/?source=vscode
"""

# 思路：预处理 + 单调栈
# 单调站： 哨兵 + 边界处理

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # preprocess
        bar_arr = [[int(item) for item in matrix[0]]]
        r, c = len(matrix), len(matrix[0])
        for i in range(1, r):
            tmp = [0] * c
            for j in range(c):
                if matrix[i][j] == "1":
                    tmp[j] = 1 + bar_arr[-1][j]
                else:
                    tmp[j] = 0
            
            bar_arr.append(tmp)
        
        # 单调栈
        def f(arr):
            extend_arr = [float('-inf')] + arr + [float('-inf')]
            stk = []
            l = [-1] * len(extend_arr)
            r = [-1] * len(extend_arr)
            for i in range(len(extend_arr)):
                while stk and extend_arr[stk[-1]] >= extend_arr[i]:
                    r[stk.pop()] = i # 找到右边界
                if stk:
                    l[i] = stk[-1] # 找到i的左边界
                stk.append(i) # 进栈
            
            # print(l ,r)
            mx = 0
            for i in range(1, len(extend_arr)-1):
                # 注意细节 r[i] - l[i] - 1
                # 当连续两个元素相等时，两个元素的累加面积会由后面一个元素得出
                mx = max(mx, (r[i] - l[i] -1)*extend_arr[i]) 
            return mx
        
        mx = 0
        for a in bar_arr:
            mx = max(mx, f(a))
        return mx