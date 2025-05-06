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
思路：

https://leetcode.cn/problems/search-a-2d-matrix/submissions/627585487/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution(object):
    # 二分法: O(logmn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        在一个已排序的二维矩阵中搜索目标值（使用左闭右开区间查找）。
        该矩阵具有以下特性：
        - 每行中的整数从左到右按升序排列。
        - 每列中的整数从上到下按升序排列。
        - 每一行的第一个整数大于前一行的最后一个整数。

        Args:
            matrix: 一个二维整数列表，表示已排序的矩阵。
            target: 需要搜索的目标整数。

        Returns:
            如果目标值存在于矩阵中，则返回 True；否则返回 False。
        """
        m, n = len(matrix), len(matrix[0])  # 获取矩阵的行数和列数

        # 将二维矩阵视为一个扁平化的一维数组进行二分查找
        # 使用左闭右开区间 [left, right)，初始时包含所有可能的索引
        left, right = 0, m * n

        # 二分查找的标准模板：循环直到 left 等于 right
        while left < right:
            mid = (left + right) // 2  # 计算中间位置在一维数组中的索引

            # 将一维数组的索引转换回二维矩阵的行和列索引
            row = mid // n
            col = mid % n

            # 获取矩阵中间位置的值
            x = matrix[row][col]

            # 根据中间值与目标值的比较结果调整搜索范围
            if x == target:
                return True  # 找到目标值，直接返回 True
            elif x < target:
                left = mid + 1  # 如果中间值小于目标值，则目标值可能在右半部分，更新 left 边界
            else:
                right = mid  # 如果中间值大于目标值，则目标值可能在左半部分，更新 right 边界

        # 循环结束时，如果没有找到目标值，则返回 False
        return False

    # O(m+n)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
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

        from typing import List