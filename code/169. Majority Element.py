'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # method 1: time complexity O(n) space complexity O(n)
        
        dic={}
        N=len(nums)
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            if dic[i]>N//2:
                return i
        
        # method 2: T O(n) S O(1)
        N=len(nums)
        cur=nums[0]
        count=0
        for i in range(N):
            if nums[i]==cur:
                count+=1
            else:
                count-=1
                if count<0:
                    cur=nums[i]
                    count=1
        return cur
        