"""[hard]
给你一个 正 整数数组 nums 。

请你求出 nums 中有多少个子数组，满足子数组中 第一个 和 最后一个 元素都是这个子数组中的 最大 值。

 

示例 1：

输入：nums = [1,4,3,3,2]

输出：6

解释：

总共有 6 个子数组满足第一个元素和最后一个元素都是子数组中的最大值：

子数组 [1,4,3,3,2] ，最大元素为 1 ，第一个和最后一个元素都是 1 。
子数组 [1,4,3,3,2] ，最大元素为 4 ，第一个和最后一个元素都是 4 。
子数组 [1,4,3,3,2] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [1,4,3,3,2] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [1,4,3,3,2] ，最大元素为 2 ，第一个和最后一个元素都是 2 。
子数组 [1,4,3,3,2] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
所以我们返回 6 。

示例 2：

输入：nums = [3,3,3]

输出：6

解释：

总共有 6 个子数组满足第一个元素和最后一个元素都是子数组中的最大值：

子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
子数组 [3,3,3] ，最大元素为 3 ，第一个和最后一个元素都是 3 。
所以我们返回 6 。

示例 3：

输入：nums = [1]

输出：1

解释：

nums 中只有一个子数组 [1] ，最大元素为 1 ，第一个和最后一个元素都是 1 。

所以我们返回 1 。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109

https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/description/
"""

# 思路很直接，但是注意细节与表达
from collections import Counter, defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        bound = [[nums[_], _, _] for _ in range(len(nums))]
        stk = []
        for i, x in enumerate(nums): # 边界求解
            while stk and nums[stk[-1]] < x:
                bound[stk[-1]][2] = i - 1
                stk.pop()
            if stk:
                if nums[stk[-1]] == nums[i]: # 处理相等情况
                    bound[i][1] = bound[stk[-1]][1]
                else:
                    bound[i][1] = stk[-1] + 1
            else:
                bound[i][1] = 0
            stk.append(i)
        for i in stk:
            bound[i][2] = len(nums) - 1
        
        # print(bound)
        bound = sorted(bound, key=lambda x:x[0])
        
        cnt = 1 # 如何统计连续相同数情况
        ans = 0
        C = lambda n: n*(n-1)//2
        for i, (x, l, r) in enumerate(bound):
            if i > 0:
                if x == bound[i-1][0] and bound[i-1][1] >= l:
                    cnt += 1
                else:
                    if cnt >= 2:
                        ans += C(cnt)
                    cnt = 1
        
        if cnt >= 2:
            ans += C(cnt)
            
        return ans + len(nums)




class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        st = [[inf, 0]]  # 无穷大哨兵
        for x in nums:
            while x > st[-1][0]:
                st.pop()
            if x == st[-1][0]:
                ans += st[-1][1]
                st[-1][1] += 1
            else:
                st.append([x, 1])
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/solutions/2738894/on-dan-diao-zhan-pythonjavacgo-by-endles-y00d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
