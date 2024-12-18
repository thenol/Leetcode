"""
[meidum]

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

 

示例 1：

输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
示例 2：

输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
示例 3：

输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2
 

提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
 

进阶：你能否用 O(n) 时间复杂度完成此题?

https://leetcode.cn/problems/wiggle-subsequence/description/?source=vscode
"""

class Solution:

    # method 2: O(n)，思路类似买卖股票
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # state: up, down分别表示摇摆序列当前时刻最后两个数的关系，up为递增关系，down为递减关系

        # initializaiton
        up, down = 1, 1
        N = len(nums)

        # transition
        for i in range(1, N):
            if nums[i-1] < nums[i]:
                # 当前为上升关系，摇摆关系依赖于前一个为下降关系
                up = down + 1 
            elif nums[i-1] > nums[i]:
                # 当前为下降关系，摇摆关系依赖与前一个为上升关系
                down = up + 1
            
            # 相等的时候，不改变 up 和 down；
            
            # 因此对于任意一个nums[i]，当前的所有 递增 或者 递减 关系都已经记录在了 up and down 里面了
            # 从而，up 和 down 可以 ❗️等价转变❗️ 为 范围状态，即 到当前位置，最长递增 和最长递减的个数

        return max(up, down)

    # method 1: O(n^2) 
    # 核心思路：和最长子序列一样，但是难点在于小细节处理
    def wiggleMaxLength1(self, nums: List[int]) -> int:
        # state: d[i] 表示以i结尾最长摇摆序列的长度
        # 0<=i<len(nums)
        N = len(nums)
        if N == 1: return N
        d = [1] * N
        tail = [0] * N # 用于记录以i为结尾反转序列的上一个整数符号

        for i in range(N):
            t = 1
            for j in range(i):
                # 易错点❌：单独处理第一个元素的情况，1<=i
                if j == 0 and nums[i]!=nums[j]:
                    d[i] = 2
                elif (nums[i] - nums[j])*tail[j] < 0:
                    d[i] = max(d[i], d[j] + 1)
                t = nums[i] - nums[j]
            tail[i] = t
        return max(d)
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        pos = [1]*N
        neg = [1]*N
        for i in range(N):
            for j in range(i):
                if 0 < nums[i] - nums[j]:
                    pos[i] = max(pos[i], neg[j] + 1)
                elif nums[i] - nums[j] < 0:
                    neg[i] = max(neg[i], pos[j] + 1)
        return max(pos + neg)
        