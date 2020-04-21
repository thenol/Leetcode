'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Fine-grained control flow of the program
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move one step each time
        N=len(nums)
        for i in range(k):
            tmp=nums[N-1]
            for j in range(N)[::-1]:
                nums[j]=nums[j-1]
            nums[0]=tmp

        # once 
        count=0
        N=len(nums)
        idx=0
        last=nums[0]
        while count<=N:
            loc=(idx+k)%N
            tmp=nums[loc]
            nums[loc]=last
            last=tmp
            idx=loc
            count+=1
            print(nums)
        # print(nums)
        '''
        [1,2,3,4,5,6]
        2
        output:
        [5,6,1,2,3,4], reason 6%2=0
        '''

        # optimization
        N=len(nums)
        count=0
        for i in range(k):
            if count>=N:
                break
            cur=(i+k)%N
            pre=nums[cur]
            nums[cur]=nums[i]
            loc=(cur+k)%N
            count+=1
            while cur!=loc and count<N:
                tmp=nums[loc]
                nums[loc]=pre
                pre=tmp
                loc=(loc+k)%N
                count+=1
                # print(nums,count)
                     

            