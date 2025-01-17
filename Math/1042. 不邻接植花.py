"""
有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，你打算种下四种花之一。

另外，所有花园 最多 有 3 条路径可以进入或离开.

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。

 

示例 1：

输入：n = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
解释：
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
示例 2：

输入：n = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]
示例 3：

输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]
 

提示：

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
每个花园 最多 有 3 条路径可以进入或离开

https://leetcode.cn/problems/flower-planting-with-no-adjacent/description/?source=vscode
"""

# 核心思路：
"""
出题人可能是受到 四色定理 的启发出的题。

问题相当于用 4 种颜色给图中的每个节点染色，要求相邻节点颜色不同。而「所有花园最多有 3 条路径可以进入或离开」，这相当于图中每个点的度数至多为 3，由于每个花园最多有 3 条路径可以进入或离开，这就说明每个花园最多有 3 个花园与之相邻，而每个花园可选的种植种类有 4 种，这就保证一定存在合法的种植方案满足题目要求
，那么只要选一个和邻居不同的颜色即可。

也就是将条件框定到了 四色定理 问题之内

最佳解法：
https://leetcode.cn/problems/flower-planting-with-no-adjacent/solutions/2227318/liang-chong-xie-fa-ha-xi-biao-shu-zu-wei-7hm8/?source=vscode
"""

from collections import deque, defaultdict
class Solution:
    # 时间复杂度：O(n+m)，其中 m 为 paths 的长度。
    # 空间复杂度：O(n+m)
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)  # 建图
        color = [0] * n
        for i, nodes in enumerate(g):
            color[i] = (set(range(1, 5)) - {color[j] for j in nodes}).pop() # 四色定理保证了，解一定存在，所以直接染色就行
        return color
            