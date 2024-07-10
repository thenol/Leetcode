"""[medium]
给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。

你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。

如果以下条件满足，我们称这些塔是 美丽 的：

1 <= heights[i] <= maxHeights[i]
heights 是一个 山脉 数组。
如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：

对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。

 

示例 1：

输入：maxHeights = [5,3,4,1,1]
输出：13
解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]  
- heights 是个山脉数组，峰值在 i = 0 处。
13 是所有美丽塔方案中的最大高度和。
示例 2：

输入：maxHeights = [6,5,3,9,2,7]
输出：22
解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山脉数组，峰值在 i = 3 处。
22 是所有美丽塔方案中的最大高度和。
示例 3：

输入：maxHeights = [3,2,5,5,2,3]
输出：18
解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
- 1 <= heights[i] <= maxHeights[i]
- heights 是个山脉数组，最大值在 i = 2 处。
注意，在这个方案中，i = 3 也是一个峰值。
18 是所有美丽塔方案中的最大高度和。
 

提示：

1 <= n == maxHeights <= 103
1 <= maxHeights[i] <= 109

https://leetcode.cn/problems/beautiful-towers-i/description/
"""
# 思路：单调站 + 前缀和，计算阶梯面积
## 单调站中存储坐标，有大用，可用来计算前后两个元素之间的距离
## 前最和可以用来计算连续数组的和

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        pre_sum = [0] * n
        stk = [-1]
        for i, item in enumerate(heights):
            while len(stk) > 1 and heights[stk[-1]] > item:
                stk.pop()
            pre_sum[i] = pre_sum[stk[-1]] + (i - stk[-1]) * item
            stk.append(i)

        re_heights = heights[::-1] 
        suf_sum = [0] * n
        stk = [-1]
        for i, item in enumerate(re_heights): # 注意这里容易犯错，就是直接heights[::-1]，然后下面直接按照heights[stk[-1]]来索引，错误很简答，就是上下没对应
            while len(stk) > 1 and re_heights[stk[-1]] > item:
                stk.pop()
            suf_sum[i] = suf_sum[stk[-1]] + (i - stk[-1]) * item
            stk.append(i)
        suf_sum = suf_sum[::-1]
        ans = 0
        for i in range(n):
            ans = max(ans, pre_sum[i] + suf_sum[i] - heights[i])
        
        return ans



class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        sufSums = [0] * n   # 后缀和数组
        st = [n]            # 单调栈, 栈底为n表示后缀和边界
        sufS = 0            # 后缀和
        for i in range(n-1, -1, -1):
            while len(st) > 1 and maxHeights[i] <= maxHeights[st[-1]]:
                # 在到达栈底n之前，弹出位于当前位置右侧的小于等于当前位置最大高度的索引
                t = st.pop()   # 获取要弹出的元素
                sufS -= maxHeights[t] * (st[-1] - t)  # 后缀和减去弹出索引对应的区间包含的高度和
                
            sufS += maxHeights[i] * (st[-1] - i)      # 后缀和累加要加入的索引对应的区间包含的高度和
            sufSums[i] = sufS      # 记录后缀和
            st.append(i)             # 元素入栈
            
        st = [-1]   # 单调栈, 栈底为-1表示前缀和边界
        res = 0     # 结果值
        preS = 0    # 前缀和
        for i, h in enumerate(maxHeights):
            while len(st) > 1 and h <= maxHeights[st[-1]]:
                # 在到达栈底-1之前，弹出位于当前位置左侧的小于等于当前位置最大高度的索引
                t = st.pop()
                preS -= maxHeights[t] * (t - st[-1])  # 前缀和和减去弹出索引对应的区间包含的高度和

            preS += h * (i - st[-1])                  # 前缀和累加要加入的索引对应的区间包含的高度和
            res = max(res, preS + sufSums[i] - h)     # 得到当前位置前后缀和，更新最大值
            st.append(i)     # 元素入栈

        return res  

# 作者：画图小匠
# 链接：https://leetcode.cn/problems/beautiful-towers-i/solutions/2617548/javapython3cqian-hou-zhui-he-dan-diao-zh-vcvo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。