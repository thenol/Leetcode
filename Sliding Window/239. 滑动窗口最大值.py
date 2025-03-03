"""
[hard]

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

https://leetcode.cn/problems/sliding-window-maximum/description/
"""

from collections import deque
from math import inf
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([]) # 单调队列
        ans = []
        for i, x in enumerate(nums):
            
            # 首先维护好固定窗口的单调队列
            while q and nums[q[-1]] < x:
                q.pop()
            q.append(i)
            if i-q[0]>=k:
                q.popleft()

            # 然后当需要输出结果的时候，就输出单调队列中取出的最大值 
            if k-1 <= i: 
                # 当 i==k-1的时候，单调队列中一定记录着窗口中的最大值
                ans.append(nums[q[0]])
        
        return ans

            
             