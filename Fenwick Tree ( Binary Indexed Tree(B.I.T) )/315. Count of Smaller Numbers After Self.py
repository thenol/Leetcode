'''
[hard]
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# version 1: brutal O(n^2) TLE

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts=[]
        for i in range(len(nums)):
            acc=0
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    acc+=1
            counts.append(acc)
        return counts


# version 2: BIT 