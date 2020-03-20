'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binsearch(arr,target):
            l,r=0,len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]>target:
                    r=mid-1
                elif arr[mid]<target:
                    l=mid+1
                elif arr[mid]==target:
                    return True
            return False
        
        start_of_right=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                start_of_right=i
        return binsearch(nums[:start_of_right],target) or binsearch(nums[start_of_right:],target)
        