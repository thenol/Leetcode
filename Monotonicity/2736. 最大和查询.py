"""
[hard]
给你两个长度为 n 、下标从 0 开始的整数数组 nums1 和 nums2 ，另给你一个下标从 1 开始的二维数组 queries ，其中 queries[i] = [xi, yi] 。

对于第 i 个查询，在所有满足 nums1[j] >= xi 且 nums2[j] >= yi 的下标 j (0 <= j < n) 中，找出 nums1[j] + nums2[j] 的 最大值 ，如果不存在满足条件的 j 则返回 -1 。

返回数组 answer ，其中 answer[i] 是第 i 个查询的答案。

 

示例 1：

输入：nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
输出：[6,10,7]
解释：
对于第 1 个查询：xi = 4 且 yi = 1 ，可以选择下标 j = 0 ，此时 nums1[j] >= 4 且 nums2[j] >= 1 。nums1[j] + nums2[j] 等于 6 ，可以证明 6 是可以获得的最大值。
对于第 2 个查询：xi = 1 且 yi = 3 ，可以选择下标 j = 2 ，此时 nums1[j] >= 1 且 nums2[j] >= 3 。nums1[j] + nums2[j] 等于 10 ，可以证明 10 是可以获得的最大值。
对于第 3 个查询：xi = 2 且 yi = 5 ，可以选择下标 j = 3 ，此时 nums1[j] >= 2 且 nums2[j] >= 5 。nums1[j] + nums2[j] 等于 7 ，可以证明 7 是可以获得的最大值。
因此，我们返回 [6,10,7] 。
示例 2：

输入：nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
输出：[9,9,9]
解释：对于这个示例，我们可以选择下标 j = 2 ，该下标可以满足每个查询的限制。
示例 3：

输入：nums1 = [2,1], nums2 = [2,3], queries = [[3,3]]
输出：[-1]
解释：示例中的查询 xi = 3 且 yi = 3 。对于每个下标 j ，都只满足 nums1[j] < xi 或者 nums2[j] < yi 。因此，不存在答案。 
 

提示：

nums1.length == nums2.length 
n == nums1.length 
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 109 
1 <= queries.length <= 105
queries[i].length == 2
xi == queries[i][1]
yi == queries[i][2]
1 <= xi, yi <= 109

https://leetcode.cn/problems/maximum-sum-queries/description/
"""
# 思路
## 本质是多元排序问题， 排序 + 单调栈二次排序 + 二分查找（有序查找问题，必然二分）
## 首先按照x排序，总体形成偏序数组，也就是部分有序，在此基础上，利用单调栈对第二个元y进行排序，
## 然后搜索时，在有序的基础之上进行搜索，有序必二分
## 注意:
##      这里query排序的目的，query本质是对有序的nums逐步扩大框定边界，
##      如果query不排序，这样顺序就是错乱的，无法保证有序的x（sorted）->有序的y（单调栈）->二分查找
"""
按照x排序后的nums数组
-
--
---
----
-----
------
|'''| query中排序后的x
|''''| 随着遍历，越往后query中的x越小，同时框定的nums范围也越大，可以保证x有序->然后用单调栈实现y有序
"""

## 二分查找相关函数

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        sortedNums = sorted([[a, b] for a, b in zip(nums1, nums2)], key = lambda x: -x[0])
        sortedQueries = sorted([[i, x, y] for i, (x, y) in enumerate(queries)], key=lambda q:-q[1])
        stack = []
        answer = [-1] * len(queries)
        j = 0
        for i, x, y in sortedQueries:
            while j < len(sortedNums) and sortedNums[j][0] >= x:
                num1, num2 = sortedNums[j]
                while stack and stack[-1][1] <= num1 + num2:
                    stack.pop()
                if not stack or stack[-1][0] < num2:
                    stack.append([num2, num1 + num2])
                j += 1
            k = bisect_left(stack, [y, 0])
            if k < len(stack):
                answer[i] = stack[k][1]
        return answer
