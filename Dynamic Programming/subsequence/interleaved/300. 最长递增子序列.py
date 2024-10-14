"""
[meidum]

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?

https://leetcode.cn/problems/longest-increasing-subsequence/description/
"""

# 思路：

# method 1: 动态规划; O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        # state: d[i] 表示以i结尾的最长严格递增子序列的长度。
        # 0<=i<len(nums)
        d = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            t = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    t = max(t, d[j] + 1) 
            d[i] = t
        return max(d)



# method 2: 动态规划+二分查找; O(nlogn)
"""
本质上以空间换时间，维护一个tail[k]，即长度为k+1的子序列的数组，
* 然后在遍历的过程中，尽可能将所有长度为 k+1 的子序列中，结尾最可能小的数存入其中
* 因为存储最小的结尾值，才能和后面的数尽可能得形成递增子序列
* tail一定是严格递增的，即tail[k+1]>tail[k]，因为每一个tail[k]存放的都是所有子序列中最小的末尾值，例如对于tail[k+1]，其长度为k的子严格递增序列中的最小值存放在 tail[k]，因此对于任意的 tail[k+1] 一定大于 tail[k]，例如[1,5,3,7]，长度为2的严格递增子序列有[1,3]，[1,5],[1,7],[5,7],[3,7]，tail[1]=3(即长度为2的严格递增子序列末尾最小值为3), 而长度为3的严格递增子序列[1,3,7]，[1,5,7]，tail[2]=7，不管是哪个子序列，tail[2]>tail[1]。
* 同时查找的过程中，用二分查找，降低时间复杂度

例如 [1,5,3]， 遍历到元素 5 时，长度为 2 的子序列尾部元素值为 5；当遍历到元素 3 时，尾部元素值应更新至 3，因为 3 遇到比它大的数字的几率更大

作者：Krahets
链接：https://leetcode.cn/problems/longest-increasing-subsequence/solutions/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

def lengthOfLIS(self, nums: List[int]) -> int:
        d = [1 for i in range(len(nums))]
        tail = [inf for item in nums]
        res = 0

        def binSearch(nums, e):
            """
            返回小于e的最大下标
            """
            lo, hi = 0, len(nums)
            while lo < hi: # 查找tail中比i小的最大值
                mi = (lo + hi) >> 1
                if e < nums[mi]:
                    hi = mi
                else:
                    lo = mi + 1
            lo = lo - 1 # lo 为不大于 e 的最大秩

            while lo>=0 and e<=nums[lo]: lo-=1 # 寻找小于e的最大秩
            
            return lo
        
        for i in range(len(nums)):
            mx_len_idx  = binSearch(tail[:res], nums[i]) # 在tail中寻找小于nums[i]的最大秩啊
            if mx_len_idx >= 0:
                d[i] = mx_len_idx + 2
            tail[d[i] - 1] = min(tail[d[i] - 1], nums[i])
            res += 1

        return max(d)
