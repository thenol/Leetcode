"""
[medium]

给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按
字典序
排列小于 arr 的最大排列。

如果无法这么操作，就请返回原数组。

 

示例 1：

输入：arr = [3,2,1]
输出：[3,1,2]
解释：交换 2 和 1
示例 2：

输入：arr = [1,1,5]
输出：[1,1,5]
解释：已经是最小排列
示例 3：

输入：arr = [1,9,4,6,7]
输出：[1,7,4,6,9]
解释：交换 9 和 7
 

提示：

1 <= arr.length <= 104
1 <= arr[i] <= 104

https://leetcode.cn/problems/previous-permutation-with-one-swap/description/?source=vscode
"""

"""
核心思路：
    * 【必要条件】：
        * 对任意的arr[i]需要找到 arr[i+1:]中小于 arr[i]的最大值 a[j]，来做交换
        * 为了让调整后的 arr 尽可能大，需要 i 尽量大，即尽量靠后
        * BF: O(N^2)
    * 【转化条件】：
        * 由于arr[i]需要尽量靠后，即 a[j] 也尽量靠后
        * 因此从后往前看，对每一个 a[j] 找寻 其左边 最近 且 最大的元素 a[i]，来交换
        * 因此，使用单调站
    * 【归纳总结】
        * 寻找 尽量靠右的 arr[i] 右边比其小的最大值 arr[j] <=> 找寻 arr[j] 左边 第一个比起大的值 arr[i] 
        * 单调站
"""

class Solution:
    # method 2: greedy
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        ...
        """https://leetcode.cn/problems/previous-permutation-with-one-swap/solutions/2202472/jiao-huan-yi-ci-de-xian-qian-pai-lie-by-evkqi/?source=vscode
        
        记数组 arr 的长度为 n，对于 0≤i<j<n，如果交换 arr[i] 和 arr[j] 后得到的新数组按字典序排列比原数组小，显然有 arr[i]>arr[j] 成立（逆序对存在的充要条件）。因此符合题意要求的交换会使得数组 arr 在下标 i 处的元素变小。那么为了得到按字典序排列小于原数组的最大新数组，尽可能地保持前面的元素不变是最优的，即让 i 最大化。

        显然在满足 arr[j]<arr[i] 的条件下，取最大的 arr[j] 是最优的。但是题目并没有元素不重复的要求，最大的 arr[j] 可能有重复值，那么选择其中下标最小的 arr[j] 是最优的。
        由前面推导可知，区间 [i+1,n) 的元素是非递减的❗️，因此我们从大到小枚举 j，直到 arr[j]<arr[i] 且 arr[j]!=arr[j−1] 成立，那么得到的 j 就是符合要求的。交换 arr[i] 和 arr[j]。


        概括：找到逆序对，然后把其中的较大者，和它右边比它小的最大的数交换
        """


    # method 1: 利用单调站，从后往前遍历找逆序对
    def prevPermOpt1_1(self, arr: List[int]) -> List[int]:
        # 单调站
        stk = [] # 非递增栈
        N = len(arr)
        right_less = [N]*N
        for i in range(N-1, -1, -1):
            while stk and arr[stk[-1]]<arr[i]: # 更新rightmost[i]，记录最大值
                right_less[i] = stk.pop()

            # trick: 本质保证了arr[i]找的是所有相同arr[j]中最右边的arr[j]
            while stk and arr[stk[-1]]==arr[i]:
                stk.pop() # 连续的数值，栈顶去重；121这种，在入栈时，会变成12，所以不用考虑
            stk.append(i)
        
        for i in range(N-1, -1, -1):
            if right_less[i] < N: # 找到最右边可以替换的逆序对
                arr[i], arr[right_less[i]] = arr[right_less[i]], arr[i]
                return arr
        
        return arr