"""
[medium]

给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。
 

示例 1：



输入: 
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出: 
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用 104 次 sumRegion 方法

https://leetcode.cn/problems/range-sum-query-2d-immutable/description/
"""

# 核心思路： 二位前缀和
# 处理技巧：哨兵护法，尤其是前缀和这种
# 最优解法：https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/2667331/tu-jie-yi-zhang-tu-miao-dong-er-wei-qian-84qp/
# 图解：https://pic.leetcode.cn/1692152740-dSPisw-matrix-sum.png


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 【本质哨兵：即人为给matrix扩展，添加一行和一列全部由0构成的元素】定义sum[i+1][j+1] 为左上角 matrix[0][0]，右下角matrix[i][j]的矩阵元素和，则
        # sum[i+1][j+1] = sum[i+1][j] + sum[i][j+1] - sum[i][j] + matrix[i][j]
        # 0<=i<=R-1, 0<=j<=C-1; 1<=i+1<=R, 1<=j+1<=C
        # 【本质哨兵】sum[1][1] 表示 左上角 matrix[0][0]，右下角matrix[0][0]的矩阵元素和，即matrix[0][0]的子数组和
        # 依赖，左，上，左上，因此顺序计算即可
        R, C = len(matrix)+1, len(matrix[0])+1
        sum = [[0 for j in range(C)] for i in range(R)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum[i+1][j+1] = sum[i+1][j] + sum[i][j+1] - sum[i][j] + matrix[i][j]
        
        self.sum = sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 求和：设子矩阵左上角matrix[r1][c1]，右下角matrix[r2-1][c2-1]，则
        # 子矩阵和 = sum[r2][c2] - sum[r2][c1] - sum[r1][c2] + sum[r1][c1]

        # 即：以[row2][col2]为右下角的矩阵和 - 以[row2][col1-1]为右下角的矩阵和 - 以[row1-1][col2]为右下角的矩阵和 + 以[row1-1][col1-1]为右下角的矩阵和
        ans = self.sum[row2+1][col2+1] - self.sum[row2+1][col1] - self.sum[row1][col2+1] + self.sum[row1][col1]
        return ans

"""
matrix:
[
    [3,0,1,4,2],
    [5,6,3,2,1],
    [1,2,0,1,5],
    [4,1,0,1,7],
    [1,0,3,0,5]
]

sum: 添加【边界哨兵护法】，含义sum[0][0]没有固定含义，sum[i+1][j+1]表示左上角[0][0]，右下角[i][j]的子数组和
[
    0 0 0 0 0 0
    0 . . . . .
    0 . . . . .
    0 . . . . .
    0 . . . . .
    0 . . . . .
]

"""

# 哨兵写法——同上；（❗️如果不请哨兵大护法写起来，边界判断将极其复杂）
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # state: d[i][j]区域matrix[:i][:j]的矩形面积
        # 0<=i<=R; 0<=j<=C
        R, C = len(matrix), len(matrix[0])

        d = [[0] * (C+1) for i in range(R+1)]

        for i in range(1, R+1):
            for j in range(1, C+1):
                d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + matrix[i-1][j-1]
        self.d = d

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 求 matrix[row1:row2+1][col1:col2+1]区域
        return self.d[row2+1][col2+1] - self.d[row1][col2+1]-self.d[row2+1][col1] + self.d[row1][col1]
