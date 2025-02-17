"""
[medium]

给定一个整数 n，即有向图中的节点数，其中节点标记为 0 到 n - 1。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。

给定两个数组 redEdges 和 blueEdges，其中：

redEdges[i] = [ai, bi] 表示图中存在一条从节点 ai 到节点 bi 的红色有向边，
blueEdges[j] = [uj, vj] 表示图中存在一条从节点 uj 到节点 vj 的蓝色有向边。
返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

 

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
 

提示：

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n

https://leetcode.cn/problems/shortest-path-with-alternating-colors/description/?source=vscode

"""

"""
最优解：https://leetcode.cn/problems/shortest-path-with-alternating-colors/solutions/2088614/bsffang-fa-tu-jie-python3shi-xian-guo-ch-82dp/?source=vscode
"""

from collections import defaultdict, deque
from dis import dis
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # d[i][j][k]表示节点i到节点j路径颜色为k的最短路径
        g = defaultdict(list)
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))

        dist = [-1] * n
        vis = {(0,0), (0, 1)} # 从0开始，红色路径和蓝色路径出发
        q = deque([(0, 0), (0, 1)]) # 从0开始，红色路径和蓝色路径出发
        level = 0

        while q:
            le = len(q)
            for i in range(le):
                x, color = q.popleft()
                if dist[x] == -1:
                    dist[x] = level

                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            
            level += 1
        
        return dist