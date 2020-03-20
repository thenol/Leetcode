'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        方法一：直接调用函数
        '''
        le=len(nums1)+len(nums2)
        med_len,med_index=(2,le//2-1) if le%2==0 else (1,le//2)
        nums3=sorted(nums1+nums2)
        if med_len==2:
            return sum(nums3[med_index:med_index+2])/2
        else:
            return nums3[med_index]
        '''
        方法二：归并框架（归并排序算法思想）
        le=len(nums1)+len(nums2)
        med_len,med_index=(2,le//2-1) if le%2==0 else (1,le//2)
        i=j=0 #
        nums3=[]
        while i<len(nums1) and j<len(nums2):
            #不变性与单调性
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        if i<len(nums1):
            nums3+=nums1[i:]
        if j<len(nums2):
            nums3+=nums2[j:]
        
        if med_len==2:
            return sum(nums3[med_index:med_index+2])/2
        else:
            return nums3[med_index]
        '''