class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def ascending_buble(nums,p):
            for i in range(len(nums),p,-1):# n-1 times
                for j in range(p+1,i-1):# i-1 times:
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            
        find=-1
        max_index=-1
        l,r=0,len(nums)-1
        i=r
        while i > l:
            j=i-1
            while j>=l:
                if nums[j]<nums[i]:
                    if j>max_index:
                        max_index=j
                        l=j
                        find=i
                j-=1
            i-=1
        nums[max_index],nums[find]=nums[find],nums[max_index]
        ascending_buble(nums,max_index)
        if find<0:
            nums.sort()
        