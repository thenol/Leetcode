"""
[hard]

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4
 

提示：

1 <= heights.length <=105
0 <= heights[i] <= 104

https://leetcode.cn/problems/largest-rectangle-in-histogram/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
和 LCR 039. 柱状图中最大的矩形 是一样的题目，只是数据范围不同而已
思路：

"""

# 单调栈重要性质：
# 1. 寻找前面或者后面第一个比当前元素小的元素
# 2. 寻找前面或者后面第一个比当前元素大的元素
# 本题本质就是寻找左右两边第一个比当前元素小的元素，从而作为边界
# 思路：对每一个数找到其左右第一个最小值，然后计算面积
# 技巧：左右哨兵的应用，可以大幅减轻代码量和出错率
# 哨兵方法可以让写的代码更少，且不容易出错，而且还节省时间
from math import inf
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = [[-inf, -1]] # 放置无穷大哨兵，这里一定要放置 [item, index]，如果只放置 index -1, 由于python的特性, heights[-1]是会索引到最后一个元素的
        heights.append(0) # 引入很小哨兵，来确保每个栈元素都能出栈，且0本省就不用考虑了
        for i, x in enumerate(heights):
            while stk[-1][0] >= x: # 细节：需要注意 大于等于 情况下就出栈；单调递增战
                ans = max(ans, stk.pop()[0]*(i-stk[-1][1]-1)) # 先pop，再读取最后一个，代码真的太简洁，精美了
            stk.append([x, i])
        
        # 最后栈里面还剩左右护法[inf,0]，不用考虑
        return ans
    

# version 2: 非哨兵版本 —— 写的很笨重且很蠢且容易出错
from math import inf
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []
        for i, x in enumerate(heights):
            while stk and heights[stk[-1]] >= x:
                idx = stk.pop()
                if stk:
                    ans = max(ans, heights[idx] * (i-stk[-1]-1))
                else:
                    ans = max(ans, heights[idx] * (i - (-1) -1))
            stk.append(i)
            
        while stk:
            idx = stk.pop()
            if stk:
                ans = max(ans, heights[idx] * (len(heights) - stk[-1] - 1))
            else:
                ans = max(ans, heights[idx] * (len(heights) - (-1) - 1))
        
        return ans


