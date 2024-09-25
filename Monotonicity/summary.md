# 单调栈
## 栈内元素单调
* 以单调递增栈为例，对每一个元素而言，左边是第一个比它小的元素，当遇到右边第一个比它小的元素时，出栈
* 当站内存储坐标时，可以计算前后两个元素之间的距离，可以用来计算阶梯面积
## 哨兵的使用
* 左哨兵可以防止遍历出界，以及非必要的空栈判断；
* 右哨兵可以确保所有元素最后都能出栈
* 哨兵demo，先放左右护法，可以参考（**85. 最大矩形.py 或者 LCR 039. 柱状图中最大的矩形.py**）
    * step 1: 单调栈中加入左护法 ```[-inf, -1]```
    * step 2: 数组中加入右护法 ```heights.append(0)```
    ```python
    from math import inf
    class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:
            ans = 0
            stk = [[-inf, -1]] # 放置无穷大哨兵，这里一定要放置 [item, index]，如果只放置 index -1, 由于python的特性, heights[-1]是会索引到最后一个元素的
            heights.append(0) # 引入很小哨兵，来确保每个栈元素都能出栈，且0本省就不用考虑了
            for i, x in enumerate(heights):
                while stk[-1][0] >= x: # 细节：需要注意 大于等于 情况下就出栈
                    ans = max(ans, stk.pop()[0]*(i-stk[-1][1]-1)) # 先pop，再读取最后一个，代码真的太简洁，精美了
                stk.append([x, i])
            
            # 最后栈里面还剩左右护法[inf,0]，不用考虑
            return ans
    ```