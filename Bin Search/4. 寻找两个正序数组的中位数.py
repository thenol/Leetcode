"""
[hard]

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 

 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

https://leetcode.cn/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/8999/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/?envType=study-plan-v2&envId=top-100-liked

空间复杂度：虽然我们用到了递归，但是可以看到这个递归属于尾递归，所以编译器不需要不停地堆栈，所以空间复杂度为 O(1)。
"""

class Solution:
    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        """
        寻找第 k 小的元素在两个排序数组中的位置
        nums1 和 nums2 分别是两个排序数组，start1 和 end1 是 nums1 的索引范围
        start2 和 end2 是 nums2 的索引范围，k 是目标位置的索引（从 1 开始）
        """
        # 计算 nums1 和 nums2 的长度
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        # 确保 len1 小于 len2，这样可以减少递归深度
        if len1 > len2:
            # 如果 nums1 长度大于 nums2，交换它们
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)

        # 如果 nums1 已经没有元素了，则直接返回 nums2 中第 k 个元素
        if len1 == 0:
            return nums2[start2 + k - 1]

        # 如果 k == 1，返回 nums1[start1] 和 nums2[start2] 中的较小值
        if k == 1:
            return min(nums1[start1], nums2[start2])

        # 计算 i 和 j，i 是 nums1 中的分割点，j 是 nums2 中的分割点
        # i 和 j 各自代表第 k/2 个元素的位置（通过 min 来避免越界）
        i = start1 + min(len1, k // 2) - 1  # nums1 的分割点
        j = start2 + min(len2, k // 2) - 1  # nums2 的分割点

        """
        可以舍弃 nums2 中的前 j + 1 个元素的原因：
            如果 nums1[i] > nums2[j]，意味着 nums1[i] 比 nums2[j] 大。换句话说，如果我们要寻找第 k 小的元素，那么 nums2[0] 到 nums2[j] 这些元素不可能包含第 k 小的元素，因为我们已经确认了 nums1[i] 比 nums2[j] 大。因此，第 k 小的元素一定在 nums2[j + 1:] 或 nums1[0:] 中。因此，我们可以舍弃 nums2 中的前 j + 1 个元素，继续在 nums1 和 nums2[j + 1:] 中查找第 k - (j - start2 + 1) 小的元素（即去掉了 nums2 前 j + 1 个元素，k 减去的就是这些元素的数量）。

            换句话说，因为 nums2[j] 是当前在 nums2 中考虑的元素之一，它比 nums1[i] 小，所以可以确定 nums2 中前 j + 1 个元素不会包含第 k 小的元素。
        """

        # 比较 nums1[i] 和 nums2[j] 的大小，决定舍弃哪个部分
        if nums1[i] > nums2[j]:
            # 如果 nums1[i] > nums2[j]，则舍弃 nums2 中的前 j+1 个元素；即 nums2[0:j+1] 一共 j+1 个元素可以确定都是较小的，可以排除掉
            # 递归寻找 nums1[start1:end1] 和 nums2[j+1:end2] 中第 k - (j - start2 + 1) 个元素
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            # 如果 nums1[i] <= nums2[j]，则舍弃 nums1 中的前 i+1 个元素；即 nums1[0:i+1] 一共 i+1 个元素可以确定都是较小的，可以排除
            # 递归寻找 nums1[i+1:end1] 和 nums2[start2:end2] 中第 k - (i - start1 + 1) 个元素
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
        
    def findMedianSortedArrays(self, nums1, nums2):
        # 获取两个数组的长度
        n, m = len(nums1), len(nums2)
        
        # 计算总数组长度的中位数位置
        # left 是总数组长度的一半，right 是总数组长度加一的一半
        left = (n + m + 1) // 2  # 奇数时，left 会多一个元素
        right = (n + m + 2) // 2  # 偶数时，right 对应的是两个中位数的平均位置

        """
        为什么加 1？
            当合并后的数组长度是奇数时，中位数的定义是数组中间的那个元素。在这种情况下，合并后的数组中，只有一个中位数，所以我们将其称为 left。
            例如，如果合并后的数组长度是 5，那么中位数是第 3 个元素，所以 left 会指向第 3 个位置。
            当合并后的数组长度是偶数时，left 会指向较左的中位数的位置。例如，合并后的数组长度是 6，left 会指向第 3 个元素。
        
        为什么加 2？
            当合并后的数组长度是偶数时，中位数是两个元素的平均值。为了正确找到这两个中位数的位置，right 需要指向第二个中位数的位置。
            例如，如果合并后的数组长度是 6，那么两个中位数是第 3 和第 4 个元素。left 会指向第 3 个位置，right 会指向第 4 个位置。
            在这种情况下，right 就是 left 之后的位置，通常情况下是两个中位数之间的分隔位置，用来计算这两个中位数的平均值。
        """
        
        # 返回两个中位数对应位置的元素的平均值
        return (self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + 
                self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) * 0.5

        


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较小的数组，以便对较小的数组进行二分查找，优化算法
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # 定义无穷大的一个大值，用于处理边界情况
        infinty = 2**40  # 设定一个足够大的数值，确保在边界时能够正确处理
        m, n = len(nums1), len(nums2)  # 获取两个数组的长度
        left, right = 0, m  # 二分查找的区间，left 是最小的索引，right 是最大的索引

        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0  # 初始化两个中位数的值

        # 二分查找：寻找一个分割点 i，使得前一部分的最大元素小于等于后一部分的最小元素
        while left <= right:
            # i 是 nums1 的分割点，j 是 nums2 的分割点
            # i 的位置由 left 和 right 计算而来，j 是通过 m 和 n 的总长度以及 i 的位置确定的
            i = (left + right) // 2  # nums1 数组的分割点
            j = (m + n + 1) // 2 - i  # nums2 数组的分割点，确保前半部分总是比后半部分多一个元素（当总数为奇数时）

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            # 这些值是分割点周围的元素，为了防止访问越界，使用无穷大和负无穷代替
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])  # nums1[i-1]，若 i == 0，则取负无穷
            nums_i = (infinty if i == m else nums1[i])  # nums1[i]，若 i == m，则取正无穷
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])  # nums2[j-1]，若 j == 0，则取负无穷
            nums_j = (infinty if j == n else nums2[j])  # nums2[j]，若 j == n，则取正无穷

            # 判断分割点是否满足条件，前一部分的最大值 <= 后一部分的最小值
            if nums_im1 <= nums_j:
                # 如果满足条件，则计算新的 median1 和 median2
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1  # 移动左边界，继续寻找更大的分割点
            else:
                right = i - 1  # 移动右边界，缩小分割范围

        # 根据 m + n 的奇偶性返回中位数
        # 如果是偶数，返回前一部分的最大值和后一部分的最小值的平均数
        # 如果是奇数，返回前一部分的最大值
        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1
