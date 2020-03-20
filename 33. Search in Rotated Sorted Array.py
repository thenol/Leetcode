class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(a,target):
            left,right=0,len(a)-1
            while left<=right:
                mid=(left+right)//2
                if a[mid]>target:
                    right=mid-1
                elif a[mid]<target:
                    left=mid+1
                elif a[mid]==target:
                    return mid
            return -1

        l,r=0,len(nums)-1
        if not nums:
            return -1
        if nums[r]>=nums[l]:
            return binSearch(nums,target)
        else:
            if nums[l]>=target:
                for i in range(len(nums)):
                    if nums[i]==target:
                        return i
                return -1
            else:
                for i in range(len(nums)-1,0,-1):
                    if nums[i]==target:
                        return i
                return -1