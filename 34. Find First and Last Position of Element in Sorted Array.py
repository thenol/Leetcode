class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        res=mid=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                res=mid
                break
        print(res)
        if res>=0:
            for i in range(mid,-1,-1): # There are two cases of the end of the loop, either a break statement or a for loop
                if not nums[i] == target:
                    break
            for j in range(mid,len(nums)):
                if not nums[j]==target:
                    break
            return [i if nums[i]==target else i+1,j if nums[j]==target else j-1] # the most important sentence !!!!!!!!!!!!!
        else:
            return [-1,-1]