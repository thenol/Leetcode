"""[hard]
给你一个下标从 0 开始的正整数数组 heights ，其中 heights[i] 表示第 i 栋建筑的高度。

如果一个人在建筑 i ，且存在 i < j 的建筑 j 满足 heights[i] < heights[j] ，那么这个人可以移动到建筑 j 。

给你另外一个数组 queries ，其中 queries[i] = [ai, bi] 。第 i 个查询中，Alice 在建筑 ai ，Bob 在建筑 bi 。

请你能返回一个数组 ans ，其中 ans[i] 是第 i 个查询中，Alice 和 Bob 可以相遇的 最左边的建筑 。如果对于查询 i ，Alice 和 Bob 不能相遇，令 ans[i] 为 -1 。

 

示例 1：

输入：heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
输出：[2,5,-1,5,2]
解释：第一个查询中，Alice 和 Bob 可以移动到建筑 2 ，因为 heights[0] < heights[2] 且 heights[1] < heights[2] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[0] < heights[5] 且 heights[3] < heights[5] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Alice 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 5 ，因为 heights[3] < heights[5] 且 heights[4] < heights[5] 。
第五个查询中，Alice 和 Bob 已经在同一栋建筑中。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
示例 2：

输入：heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
输出：[7,6,-1,4,6]
解释：第一个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[0] < heights[7] 。
第二个查询中，Alice 和 Bob 可以移动到建筑 6 ，因为 heights[3] < heights[6] 且 heights[5] < heights[6] 。
第三个查询中，Alice 无法与 Bob 相遇，因为 Bob 不能移动到任何其他建筑。
第四个查询中，Alice 和 Bob 可以移动到建筑 4 ，因为 heights[3] < heights[4] 且 heights[0] < heights[4] 。
第五个查询中，Alice 可以直接移动到 Bob 的建筑，因为 heights[1] < heights[6] 。
对于 ans[i] != -1 ，ans[i] 是 Alice 和 Bob 可以相遇的建筑中最左边建筑的下标。
对于 ans[i] == -1 ，不存在 Alice 和 Bob 可以相遇的建筑。
 

提示：

1 <= heights.length <= 5 * 104
1 <= heights[i] <= 109
1 <= queries.length <= 5 * 104
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1

https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/description/
"""
# 本质：求解 两个元素 右边第一个大的元素
# 思路：特殊处理降低复杂度，转化为 一元 求右边第一个大的元素，即降元
## step 1: 判断基本case，也就是 i < j && heights[i]<heights[j] 的情况，此时直接满足条件
## step 2: 如果不满足上述情况，即 i < j && heights[i]>=heights[j] 时，右边第一个大的元素完全由 heights[i] 决定, 此时用单调栈

from heapq import heappop, heappush
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        left = [[] for _ in heights]
        for qi, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i  # 保证 i <= j
            if i == j or heights[i] < heights[j]:
                ans[qi] = j  # i 直接跳到 j
            else:
                left[j].append((heights[i], qi))  # 离线

        h = []
        for i, x in enumerate(heights):  # 从小到大枚举下标 i
            while h and h[0][0] < x:
                ans[heappop(h)[1]] = i  # 可以跳到 i（此时 i 是最小的）
            for p in left[i]: # 为什么先出堆，再入堆：将i之前的所有元素如堆，然后后面再回答，在也就是后面遍历的下标 k>i，来满足条件 k>i, k>j, 同时 heights[k]>heights[i], heights[k]>heights[j]
                heappush(h, p)  # 后面再回答
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/solutions/2533058/chi-xian-zui-xiao-dui-pythonjavacgo-by-e-9ewj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。