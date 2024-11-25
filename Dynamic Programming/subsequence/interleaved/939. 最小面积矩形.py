"""
[medium]

给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

 

示例 1：

输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
输出：4
示例 2：

输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出：2
 

提示：

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
所有的点都是不同的。

https://leetcode.cn/problems/minimum-area-rectangle/description/?source=vscode
"""
# 非常能揭示01背包，当背包不加限制的情况下，和子序列之间完全等价

# 另外如果只关注：1）如何构成矩形；2）如何求最小；这样的思路也很难
# ✅最佳的情况是：暴力->动态规划->如何定状态，并且缩减规模


from math import inf
class Solution:
    # method 1: 任意子序列问题
    # 无条件=>子序列问题=>01背包下的，背包无限大情况
    def minAreaRect(self, points: List[List[int]]) -> int:
        # state: d[i]表示以points[:i]范围的最小矩形面积
        # 0<=i<=N
        N = len(points)
        s = set(tuple(item) for item in points)
        d = [inf]*(N+1)

        for i in range(N+1):
            x1, y1 = points[i-1]
            d[i] = d[i-1] # 不过不选择i-1；
            for j in range(i):
                x2, y2 = points[j]
                if x1!=x2 and y1!=y2 and (x1, y2) in s and (x2, y1) in s:
                    # 检测是否可以构成矩形
                    d[i] = min(d[i], abs((y1-y2)*(x1-x2)))
        return d[N] if d[N]<inf else 0


    """
    换句话说，这里子元素，可选可不选，或者说可能构成了最优解，或者可能未参与构成最优解；
    但是《769. 最多能完成排序的块.py》中的每个子元素都对最优解产生了影响，因此必然得选，所以不存在这一步“不选择的”抉择：d[i] = d[i-1]
    """
