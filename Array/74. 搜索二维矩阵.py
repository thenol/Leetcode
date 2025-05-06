"""
[medium]

给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

https://leetcode.cn/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-100-liked
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
