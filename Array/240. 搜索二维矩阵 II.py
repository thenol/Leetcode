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

https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/3076084/er-fen-cha-zhao-ologmlogn-by-7kuai-qian-p3ep2/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution(object):
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


        # 二分搜索
        # 时间复杂度 O(log(m)+log(n)) = O(log(m*n))
        def binarysearch(a_l, a_r, b_l, b_r):
            """
            对给定的二维排序矩阵的子区域执行递归的二分搜索，以查找目标值。

            该函数将矩阵的一个矩形区域定义为搜索空间，并通过比较中间元素与目标值来缩小搜索范围。
            由于矩阵是按行和列排序的，因此可以将搜索空间划分为四个可能的子区域。

            参数:
                a_l (int): 当前搜索区域左上角的行索引（起始行）。
                a_r (int): 当前搜索区域左上角的列索引（起始列）。
                b_l (int): 当前搜索区域右下角的行索引（结束行）。
                b_r (int): 当前搜索区域右下角的列索引（结束列）。

            返回:
                bool: 如果在当前搜索区域或其任何子区域中找到目标值，则返回 True；否则返回 False。
            """
            # 说白了，以矩阵 区域 为单位进行二分搜索
            # 左上[a_l, a_r] 右下[b_l, b_r]

            # 基本情况：检查当前搜索区域是否有效。如果左上角的行索引大于右下角的行索引，
            # 或者左上角的列索引大于右下角的列索引，则表示当前区域为空，目标值不可能存在。
            if a_l <= b_l and a_r <= b_r:
                # 计算当前搜索区域的中间元素的行索引和列索引。
                mid_l = (a_l + b_l) // 2
                mid_r = (a_r + b_r) // 2

                # 检查中间元素是否等于目标值。如果是，则已找到目标值，返回 True。
                if matrix[mid_l][mid_r] == target:
                    return True
                # 如果中间元素大于目标值，则目标值可能存在于当前区域的左上角或右上角这两个子区域中。
                # 因此，我们对这两个子区域递归调用 binarysearch 函数。
                elif matrix[mid_l][mid_r] > target:
                    # 搜索左上子区域：行范围不变 (a_l 到 mid_l-1)，列范围不变 (a_r 到 b_r)。
                    # 搜索右上子区域：行范围不变 (mid_l 到 b_l)，列范围缩小 (a_r 到 mid_r-1)。
                    return binarysearch(a_l, a_r, mid_l-1, b_r) or binarysearch(mid_l, a_r, b_l, mid_r-1)
                # 如果中间元素小于目标值，则目标值可能存在于当前区域的左下角或右下角这两个子区域中。
                # 因此，我们对这两个子区域递归调用 binarysearch 函数。
                else:
                    # 搜索左下子区域：行范围缩小 (mid_l+1 到 b_l)，列范围不变 (a_r 到 b_r)。
                    # 搜索右下子区域：行范围不变 (a_l 到 mid_l)，列范围缩小 (mid_r+1 到 b_r)。
                    return binarysearch(mid_l+1, a_r, b_l, b_r) or binarysearch(a_l, mid_r+1, mid_l, b_r)

            # 如果最初传入的搜索区域无效（例如，左上角在右下角下方或右方），
            # 或者递归调用后所有可能的子区域都已搜索完毕但未找到目标值，则返回 False。
            return False

        # 获取输入矩阵的行数 (m) 和列数 (n)。
        m, n = len(matrix), len(matrix[0])
        # 调用 binarysearch 函数，从整个矩阵的左上角 (0, 0) 到右下角 (m-1, n-1) 开始搜索目标值。
        return binarysearch(0, 0, m-1, n-1)


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