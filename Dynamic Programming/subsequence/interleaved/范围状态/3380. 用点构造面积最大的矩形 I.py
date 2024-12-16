"""
[medium]

给你一个数组 points，其中 points[i] = [xi, yi] 表示无限平面上一点的坐标。

你的任务是找出满足以下条件的矩形可能的 最大 面积：

矩形的四个顶点必须是数组中的 四个 点。
矩形的内部或边界上 不能 包含任何其他点。
矩形的边与坐标轴 平行 。
返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。

 

示例 1：

输入： points = [[1,1],[1,3],[3,1],[3,3]]

输出：4

解释：

示例 1 图示

我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。

示例 2：

输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

输出：-1

解释：

示例 2 图示

唯一一组可能构成矩形的点为 [1,1], [1,3], [3,1] 和 [3,3]，但点 [2,2] 总是位于矩形内部。因此，返回 -1 。

示例 3：

输入： points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

输出：2

解释：

示例 3 图示

点 [1,3], [1,2], [3,2], [3,3] 可以构成面积最大的矩形，面积为 2。此外，点 [1,1], [1,2], [3,1], [3,2] 也可以构成一个符合题目要求的矩形，面积相同。

 

提示：

1 <= points.length <= 10
points[i].length == 2
0 <= xi, yi <= 100
给定的所有点都是 唯一 的。

https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-i/description/
"""

# 核心思路和最小面积矩形相同

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        # state: d[i]表示points[:i]范围最大矩形
        # 0<=i<=N
        N  = len(points)
        d = [-1] * (N+1)
        points_set = set(tuple(item) for item in points)
        
        def check(p1, p2, points_set):
            if p1[0] == p2[0] or p1[1] == p2[1]: return False # 只需要找对角线
            x1, y1 = p1
            x2, y2 = p2
            p3 = tuple([x1, y2])
            p4 = tuple([x2, y1])
            if p3 in points_set \
            and p4 in points_set:
                for x, y in points_set:
                    if (x, y) != tuple(p1) \
                    and (x,y) != tuple(p2) \
                    and (x, y) not in set({p3, p4})\
                    and (min(x1, x2)<=x<=max(x1, x2) and min(y1,y2)<=y<=max(y1,y2)):
                        return False
            else:
                return False
            return True
            
        
        # transition
        for i in range(1, N+1):
            d[i] = d[i-1] # 当前点不选择
            for j in range(i): # 可以选择当前点
                # if i==4 and j==1:
                #     print(points[i-1], points[j-1])
                #     print(check(points[i-1], points[j-1], points_set))
                if check(points[i-1], points[j-1], points_set):
                    d[i] = max(d[i], abs(points[i-1][0]-points[j-1][0])*abs(points[i-1][1]-points[j-1][1]))
        
        return d[N]
                
            
        