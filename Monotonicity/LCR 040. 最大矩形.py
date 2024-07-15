"""[hard]
给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。

注意：此题 matrix 输入格式为一维 01 字符串数组。

 

示例 1：

"10100"
"10111"
"11111"
"10010"

输入：matrix = ["10100","10111","11111","10010"]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = ["0"]
输出：0
示例 4：

输入：matrix = ["1"]
输出：1
示例 5：

输入：matrix = ["00"]
输出：0
 

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

https://leetcode.cn/problems/PLYXKQ/description/
"""
# 思路：预处理 + 柱状图中最大的矩形 LCR 039


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = 0 if matrix[i][j] == "0" else dp[i-1][j]+int(matrix[i][j])
        
        ans = 0
        for nums in dp:
            ans = max(ans, self.maxS(nums))
        
        return ans

    
    def maxS(self, nums):
        stk = [[-2, -1]] # 左右护法哨兵，单调递增栈，注意哨兵构造
        nums.append(-1)
        ans = 0
        for i, x in enumerate(nums):
            while stk[-1][0] >= x: # 
                ans = max(ans, stk.pop()[0]*(i-stk[-1][1] - 1))
            stk.append([x, i])
        
        return ans