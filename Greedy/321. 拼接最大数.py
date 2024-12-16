"""
[hard]

给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。

请你利用这两个数组中的数字中创建一个长度为 k <= m + n 的最大数，在这个必须保留来自同一数组的数字的相对顺序。

返回代表答案的长度为 k 的数组。

 

示例 1：

输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
输出：[9,8,6,5,3]
示例 2：

输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
输出：[6,7,6,0,4]
示例 3：

输入：nums1 = [3,9], nums2 = [8,9], k = 3
输出：[9,8,9]
 

提示：

m == nums1.length
n == nums2.length
1 <= m, n <= 500
0 <= nums1[i], nums2[i] <= 9
1 <= k <= m + n

https://leetcode.cn/problems/create-maximum-number/description/?source=vscode
"""

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def f1(num, k):
            """选取k个数"""
            remainder = len(num) - k
            stk = []

            for n in num:
                while stk and remainder and stk[-1] < n: # ⭕️ 退出条件可能是两个，不一定能删完
                    stk.pop()
                    remainder -= 1
                stk.append(n)
            
            return stk[:k] # ⭕️ 如果没删完，必须只能选取前k个

        def merge(A, B):
            ans = []
            while A or B:
                if A < B:
                    ans.append(B.pop(0))
                else:
                    ans.append(A.pop(0))
            return ans
        
        return max(
            merge(f1(nums1, k1), f1(nums2, k-k1)) for k1 in range(k+1) if k1 <= len(nums1) and k-k1 <=len(nums2)  # ⭕️ 这里 k1的范围应该是 range(k+1)，否则会导致nums2为空的情况选不到
        )