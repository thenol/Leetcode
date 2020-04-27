'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1: need to control two pointers, tougher and easy to be wrong

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        le=sm=l=r=0
        N=len(nums)
        mn=N+1
        while r<N or sm>=s:# loop ending: r==N && sm<s 
            if sm<s:
                sm+=nums[r]
                r+=1
                le+=1
            else:
                mn=min(mn,le)
                sm-=nums[l]
                l+=1
                le-=1
        # print(nums[l],nums[r-1],sm)
        if sm>=s:
            mn=min(mn,le)
        if mn==N+1:
            mn=0
        return mn
        

# version 2: only need to control one pointer, simpler
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = total = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= s:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return  0 if ans == len(nums) + 1 else ans

# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/209-chang-du-zui-xiao-de-zi-shu-zu-hua-dong-chua-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。