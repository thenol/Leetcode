"""
[hard]

给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。

 

示例 1：


输入：matrix = [[1,0,1],[0,-2,3]], k = 2
输出：2
解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
示例 2：

输入：matrix = [[2,2,-1]], k = 3
输出：3
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 

进阶：如果行数远大于列数，该如何设计解决方案？

https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/description/?source=vscode
"""

# 核心思路：
"""


https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/solutions/51496/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
"""
from math import inf
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:


# TLE 预处理 + 暴力版
# 时间复杂度 O(M^2N^2) TLE version
from math import inf
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        s = self.init(matrix, M, N)
        mx = -inf

        # print(s)
        for i in range(M):
            for j in range(N):
                for h in range(i+1):
                    for g in range(j+1):
                        sm = self.sum_region(h, g, i, j, s) 
                        if mx < sm <= k:
                            mx = sm
        
        return mx

    def init(self, matrix, M, N):
        # ❗️❗️❗️state: s[i][j] 表示
        # 以matrix[:i][:j]区域的面积和，也就是以matrix[0][0]为左上角，
        # 以matrix[i-1][j-1]为右下角的矩形区域之和
        # 0<=i<=R, 0<=j<=C
        s = [[0] * (N+1) for i in range(M+1)]

        # initialization
        ...

        # transition
        # matrix上矩形之间关系的动态规划
        for i in range(1, M+1):
            for j in range(1, N+1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + matrix[i-1][j-1]
        
        return s
    
    def sum_region(self, r1, c1, r2, c2, s):
        """
        易错点❌：注意这里理解的r,c为matrix坐标，需要转换成s中的坐标关系
        读取以matrix[r1][c1]为左上角，那么对应s中以matrix[r1][c1]为右下角的矩形面积为s[r1+1][c1+1]，matrix[r2][c2]为右下角，那么对应s中以matrix[r2][c2]为右下角的矩形面积为s[r2+1][c2+1]的矩形的面积
        """
        ans = s[r2+1][c2+1] - s[r2+1][c1+1-1] - s[r1+1-1][c2+1] + s[r1+1-1][c1+1-1]

        # 画图理解
        return ans