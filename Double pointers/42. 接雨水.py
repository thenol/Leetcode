"""
[hard]

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

https://leetcode.cn/problems/trapping-rain-water/description/
"""
"""
最优解法：https://leetcode.cn/problems/trapping-rain-water/solutions/1974340/zuo-liao-nbian-huan-bu-hui-yi-ge-shi-pin-ukwm/
"""

class Solution:
    # 单调栈：O(1N)：构成单调递减栈
    # idea: 
    """
    上面的方法相当于「竖着」计算面积，单调栈的做法相当于「横着」计算面积。
    这个方法可以总结成 16 个字：找上一个更大元素，在找的过程中填坑。
    注意 while 中加了等号，这可以让栈中没有重复元素，从而在有很多重复元素的情况下，使用更少的空间。


    # 柱状图：
    # |
    # |       |
    # | |   | |   | | |   | | | | |
    # | | | | | | | | | | | | | | |
    """
    def trap(self, height: List[int]) -> int:
        """
        计算数组表示的柱状图中可以积攒的雨水总量。

        Args:
            height: 一个整数列表，表示柱状图中每个柱子的高度。

        Returns:
            一个整数，表示积攒的雨水总量。
        """
        ans = 0  # 初始化雨水总量
        st = []  # 初始化一个栈，用于存储柱子的索引
        for i, h in enumerate(height):  # 遍历每个柱子及其索引
            # 当栈不为空且当前柱子的高度大于等于栈顶柱子的高度时，说明可以形成一个凹槽
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]  # 弹出栈顶柱子的高度，作为凹槽的底部高度
                if not st:  # 如果栈为空，说明左边没有更高的柱子，无法形成凹槽，跳出循环；很巧妙，有了这一步，就不用加哨兵了
                    break
                left = st[-1]  # 获取新的栈顶柱子的索引，作为凹槽的左边界
                # 计算当前凹槽可以积攒的水的高度，取决于左右两侧较低的柱子的高度减去底部的高度
                dh = min(height[left], h) - bottom_h # 每次发现凹槽，就计算一次
                # 计算当前凹槽可以积攒的水的宽度，即当前柱子的索引减去左边界的索引再减1
                ans += dh * (i - left - 1)  # 将当前凹槽积攒的水量加到总雨水总量中；⭕️注意为什么是这样计算方式，而不是直接 dh * 1，因为是 横着填
            st.append(i)  # 将当前柱子的索引压入栈中
        return ans  # 返回总的雨水总量

    # O(1N)双指针:
    # idea：当前盛水量，取决于两侧较矮的柱子
    # 竖着计算含水量
    def trap(self, height: List[int]) -> int:
        ans = left = pre_max = suf_max = 0
        right = len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left]) # 左侧最高柱子
            suf_max = max(suf_max, height[right]) # 右侧最高柱子

            """
            为什么移动低的柱子，保留高的柱子
            可以联想单指针的情况，目的就是对任意对元素 i 都需要招到其左右两侧最高对柱子，因此必须保留招到对最高的柱子
            """
            if pre_max < suf_max: # 如果左侧的柱子更低
                ans += pre_max - height[left] # 则当前盛水量取决于短板效应，也就是左侧最高柱子
                left += 1 # 算完继续右移
            else:
                ans += suf_max - height[right] # 如果右侧柱子更低，则盛水量取决于右侧最高柱子
                right -= 1 # 算完向左移动
        
        return ans


    # O(3N)单指针: 左右两侧分别max，3躺遍历
    # idea：当前盛水量，取决于左右两侧最高的柱子
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_mx = []
        lm = 0
        for i, x in enumerate(height):
            lm = max(lm, x)
            left_mx.append(lm)
        
        right_mx = []
        rm = 0
        for i, x in enumerate(reversed(height)):
            rm = max(rm, x)
            right_mx.append(rm)
        
        right_mx = right_mx[::-1]

        ans = 0
        for i in range(n):
            ans += min(left_mx[i], right_mx[i]) - height[i]
        
        return ans
        



        
