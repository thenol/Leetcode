"""
[medium]

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 

示例 1：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109

https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
相似题目 74
思路：

https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/3076084/er-fen-cha-zhao-ologmlogn-by-7kuai-qian-p3ep2/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution(object):
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1  # 从右上角开始
        while i < m and j >= 0:  # 还有剩余元素
            if matrix[i][j] == target:
                return True  # 找到 target
            if matrix[i][j] < target:
                i += 1  # 这一行剩余元素全部小于 target，排除
            else:
                j -= 1  # 这一列剩余元素全部大于 target，排除
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binsearch(ar: int, ac: int, br: int, bc: int) -> bool:
            """
            递归地在子矩阵中进行二分查找。

            Args:
                ar: 子矩阵的起始行索引。
                ac: 子矩阵的起始列索引。
                br: 子矩阵的结束行索引。
                bc: 子矩阵的结束列索引。

            Returns:
                如果目标值存在于子矩阵中，则返回 True；否则返回 False。
            """
            # 如果子矩阵为空，则目标值不存在
            if ar > br or ac > bc:
                return False

            # 计算子矩阵的中间元素的行索引和列索引
            mr = (ar + br) >> 1  # 等价于 (ar + br) // 2，位运算更高效
            mc = (ac + bc) >> 1  # 等价于 (ac + bc) // 2，位运算更高效

            # 如果找到目标值，直接返回 True
            if matrix[mr][mc] == target:
                return True
            # 如果目标值小于中间元素，则可能在左上或左下两个子矩阵中
            elif target < matrix[mr][mc]: # 比 matrix[mr][mc] 小的，可能是上半部分，和左下部分
                # 搜索上半子矩阵 [ar, ac] 到 [mr-1, bc]
                # 或搜索左下子矩阵 [mr, ac] 到 [br, mc-1]
                return binsearch(ar, ac, mr - 1, bc) or binsearch(mr, ac, br, mc - 1)
            # 如果目标值大于中间元素，则可能在右上或右下两个子矩阵中
            else:  # target > matrix[mr][mc] # # 比 matrix[mr][mc] 大的，可能是下半部分，和右上部分
                # 搜索下半子矩阵 [mr+1, ac] 到 [br, bc]
                # 或搜索右上子矩阵 [ar, mc+1] 到 [mr, bc]
                return binsearch(mr + 1, ac, br, bc) or binsearch(ar, mc + 1, mr, bc)

        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        # 从整个矩阵的左上角 (0, 0) 到右下角 (m-1, n-1) 开始进行二分查找
        return binsearch(0, 0, m - 1, n - 1)



"""
[
    [1, 4, 7, 11,15],
    [2, 5, 8, 12,19],
    [3, 6, 9, 16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 11

n = 300
matrix = [[1] * (n - 1 - i) + [9] * (i + 1) for i in range(n)]
target = 5

"""