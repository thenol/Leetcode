"""
[medium]

返回所有长度为 n 且满足其每两个连续位上的数字之间的差的绝对值为 k 的 非负整数 。

请注意，除了 数字 0 本身之外，答案中的每个数字都 不能 有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 3, k = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。
示例 2：

输入：n = 2, k = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
示例 3：

输入：n = 2, k = 0
输出：[11,22,33,44,55,66,77,88,99]
示例 4：

输入：n = 2, k = 2
输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
 

提示：

2 <= n <= 9
0 <= k <= 9

https://leetcode.cn/problems/numbers-with-same-consecutive-differences/description/?source=vscode
"""

from functools import cache
class Solution:
    # method 2: 代码简化
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        @cache
        def f(i, pre, last):
            nonlocal n, k
            if i == n:  # 递归终止条件
                return ['']  # 返回空字符串作为终结标志
            
            ans = []
            for d in range(10):
                if pre and not d: continue
                if (last == -1 or abs(d - last) == k):  # 判断数字是否符合差值条件
                    next_items = f(i + 1, 0, d)  # 递归到下一层
                    ans.extend([str(d) + item for item in next_items])  # 连接当前数字和子序列；注意❗️：解一定存在，所以这里其实本质上，不需要判断 next_items 是否存在
            return ans
        
        return [int(item) for item in f(0, 1, -1)]

    # method 1: 数位dp
    def numsSameConsecDiff_1(self, n: int, k: int) -> List[int]:
        # @cache
        # def f(i, mask, pre, is_limit):
        #     """当前i为；已经选择了mask;pre前导0；是否受限"""

        @cache
        def f(i, pre, last):
            nonlocal n, k
            # initialization
            ... # 使用多成功状态返回
            
            # transition
            ans = []
            for d in range(10):
                if pre and not d: continue
                if i==n:
                    if -1 != last: # last != -1 and abs(d-last)==k
                        if abs(d-last)==k:
                            ans.append(str(d))
                    else: # last == -1
                        ans.append(str(d))

                    # 因此简化条件 last == -1 or (last != -1 and abs(d-last)==k)
                    # 也就是 last == -1 or abs(d-last)==k
                else:
                    tmp = []
                    if -1 != last:
                        if abs(d-last)==k:
                            tmp = f(i+1, 0, d)
                    else:
                        tmp = f(i+1, 0, d)
                    for item in tmp:
                        ans.append(str(d)+str(item))
            return ans
        ans = f(1, 1, -1)
        return [int(item) for item in ans]
