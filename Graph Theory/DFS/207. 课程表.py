"""
[medium]

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
 

提示：

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同

https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：检测图是否存在环
方法：三色标记法

https://leetcode.cn/problems/course-schedule/solutions/2992884/san-se-biao-ji-fa-pythonjavacgojsrust-by-pll7/?envType=study-plan-v2&envId=top-100-liked
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否能够完成所有课程的学习。

        Args:
            numCourses: 课程总数。
            prerequisites: 一个列表，其中每个元素是一个包含两个整数的列表 [a, b]，
                           表示学习课程 a 之前必须先学习课程 b。

        Returns:
            如果能够完成所有课程，则返回 True；否则返回 False。
        """
        # 创建一个邻接表来表示课程之间的依赖关系
        # g[i] 存储的是学习课程 i 之前需要学习的所有课程的列表
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)  # 课程 b 是课程 a 的先修课程，所以在 b 的邻接表中添加 a

        # 使用颜色标记节点的状态，用于检测环
        # 0: 未访问
        # 1: 正在访问中
        # 2: 已完成访问
        colors = [0] * numCourses

        def dfs(x: int) -> bool:
            """
            深度优先搜索函数，用于检测从节点 x 开始是否存在环。

            Args:
                x: 当前访问的课程。

            Returns:
                如果存在环，则返回 True；否则返回 False。
            """
            colors[x] = 1  # 将当前节点标记为正在访问中

            # 遍历当前课程 x 的所有后继课程 y (即学习 x 之后需要学习的课程)
            for y in g[x]:
                # 如果后继课程 y 正在被访问 (colors[y] == 1)，说明存在环
                # 或者后继课程 y 未被访问 (colors[y] == 0) 且从 y 开始的 DFS 发现了环
                if colors[y] == 1 or (colors[y] == 0 and dfs(y)):
                    return True  # 找到了环

            colors[x] = 2  # 将当前节点标记为已完成访问
            return False  # 从当前节点开始没有找到环

        # 遍历所有课程
        for i, c in enumerate(colors):
            # 如果当前课程未被访问 (颜色为 0)，并且从该课程开始的 DFS 发现了环
            if c == 0 and dfs(i):
                return False  # 存在环，无法完成所有课程

        # 如果遍历完所有课程都没有发现环，则可以完成所有课程
        return True  # 没有环