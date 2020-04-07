'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# method 1: dynamic programming

# The last state is d [i], which represents the maximum cumulative product of consecutive sequences ending in nums [i]
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dynamic programming
        d=nums[:]
        for j in range(1,len(nums)):
            d[j]=max(d[j],d[j-1]*d[j])
        return max(d)

# But the result is wrong because the sequence is not monotonically increasing

# Method 2: Optimized brute force method, which is obtained using the form filling method, usually used in dynamic programming
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        N=len(nums)
        d=[[nums[i] if i==j else '0' for j in range(N)] for i in range(N)]
        
        # optimal brutal method
        for i in range(N-1,-1,-1):
            for j in range(i,N):
                if j>i:
                    d[i][j]=d[i][i]*d[i+1][j]
                ans=d[i][j] if d[i][j]>ans else ans

        # print(d)
        return ans

# Method 3: 


